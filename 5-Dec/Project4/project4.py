import os
import json
import uuid
from datetime import datetime
import pandas as pd
import pymysql

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "DipsuAnk2016"
DB_NAME = "billing_app"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_CSV = os.path.join(BASE_DIR, "catalog.csv")
BILL_JSON = os.path.join(BASE_DIR, "bill_input.json")


def log(msg: str):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {msg}")


def ensure_catalog_csv(path: str = CATALOG_CSV):
    if os.path.exists(path):
        log(f"Found catalog CSV: {os.path.abspath(path)}")
        return

    log("catalog.csv not found. Creating a default catalog...")
    data = [
        {"sku": "P1001", "name": "Notebook", "price": 50.00, "tax_pct": 12},
        {"sku": "P1002", "name": "Pencil", "price": 10.00, "tax_pct": 0},
        {"sku": "P1003", "name": "Backpack", "price": 1200.00, "tax_pct": 18},
        {"sku": "P1004", "name": "Water Bottle", "price": 250.00, "tax_pct": 12},
        {"sku": "P1005", "name": "Desk Lamp", "price": 799.00, "tax_pct": 18},
        {"sku": "P1006", "name": "Pen Set", "price": 199.00, "tax_pct": 12},
    ]
    df = pd.DataFrame(data)
    df.to_csv(path, index=False, encoding="utf-8")
    log(f"Created catalog CSV at: {os.path.abspath(path)}")


def ensure_bill_json(path: str = BILL_JSON):
    if os.path.exists(path):
        log(f"Found bill JSON: {os.path.abspath(path)}")
        return

    log("bill_input.json not found. Creating a default bill...")
    bill = {
        "customer": {"name": "Rahul Sharma", "phone": "9000000001"},
        "items": [
            {"sku": "P1001", "qty": 3, "discount_pct": 0},
            {"sku": "P1003", "qty": 1, "discount_pct": 5},
            {"sku": "P1004", "qty": 2, "discount_pct": 10}
        ],
        "global_discount_pct": 2
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(bill, f, indent=2)
    log(f"Created bill JSON at: {os.path.abspath(path)}")


def connect_server():
    return pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, autocommit=True)


def ensure_billing_db_and_tables():
    conn = connect_server()
    try:
        with conn.cursor() as cur:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            log(f"Ensured database exists: {DB_NAME}")
            cur.execute(f"USE {DB_NAME}")

            cur.execute("""
                CREATE TABLE IF NOT EXISTS invoices (
                  invoice_id INT AUTO_INCREMENT PRIMARY KEY,
                  invoice_no VARCHAR(30) UNIQUE,
                  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                  customer_name VARCHAR(150) NOT NULL,
                  customer_phone VARCHAR(20),
                  subtotal DECIMAL(12,2) NOT NULL,
                  discount_total DECIMAL(12,2) NOT NULL,
                  tax_total DECIMAL(12,2) NOT NULL,
                  grand_total DECIMAL(12,2) NOT NULL,
                  notes VARCHAR(255)
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS invoice_items (
                  item_id INT AUTO_INCREMENT PRIMARY KEY,
                  invoice_id INT NOT NULL,
                  sku VARCHAR(30) NOT NULL,
                  name VARCHAR(150) NOT NULL,
                  qty INT NOT NULL,
                  unit_price DECIMAL(12,2) NOT NULL,
                  discount_pct DECIMAL(5,2) NOT NULL DEFAULT 0,
                  tax_pct DECIMAL(5,2) NOT NULL DEFAULT 0,
                  line_subtotal DECIMAL(12,2) NOT NULL,
                  line_discount DECIMAL(12,2) NOT NULL,
                  line_tax DECIMAL(12,2) NOT NULL,
                  line_total DECIMAL(12,2) NOT NULL,
                  CONSTRAINT fk_item_invoice FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
                  INDEX idx_invoice (invoice_id)
                )
            """)
            log("Ensured tables exist: invoices, invoice_items")
    finally:
        conn.close()


def connect_db():
    return pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=DB_NAME,
                           autocommit=False)


def load_catalog(path: str = CATALOG_CSV) -> pd.DataFrame:
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("Catalog CSV is empty.")

    required = {"sku", "name", "price", "tax_pct"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Catalog CSV missing required columns: {missing}")

    df["sku"] = df["sku"].astype(str)
    df["name"] = df["name"].astype(str)
    df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0.0)
    df["tax_pct"] = pd.to_numeric(df["tax_pct"], errors="coerce").fillna(0.0)
    return df.set_index("sku")


def load_bill(path: str = BILL_JSON) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def compute_invoice(catalog_df: pd.DataFrame, bill: dict) -> dict:
    items_out = []
    subtotal = discount_total = tax_total = 0.0

    for it in bill.get("items", []):
        sku = str(it["sku"])
        qty = int(it["qty"])
        discount_pct = float(it.get("discount_pct", 0.0))

        if sku not in catalog_df.index:
            raise ValueError(f"SKU not in catalog: {sku}")

        row = catalog_df.loc[sku]
        name = row["name"]
        unit_price = float(row["price"])
        tax_pct = float(row["tax_pct"])

        line_subtotal = qty * unit_price
        line_discount = line_subtotal * (discount_pct / 100.0)
        line_taxable = line_subtotal - line_discount
        line_tax = line_taxable * (tax_pct / 100.0)
        line_total = line_taxable + line_tax

        subtotal += line_subtotal
        discount_total += line_discount
        tax_total += line_tax

    items_out.append({
        "sku": sku, "name": name, "qty": qty,
        "unit_price": round(unit_price, 2),
        "discount_pct": round(discount_pct, 2),
        "tax_pct": round(tax_pct, 2),
        "line_subtotal": round(line_subtotal, 2),
        "line_discount": round(line_discount, 2),
        "line_tax": round(line_tax, 2),
        "line_total": round(line_total, 2),
    })

    global_pct = float(bill.get("global_discount_pct", 0.0))
    taxable_base = subtotal - discount_total
    global_discount_value = taxable_base * (global_pct / 100.0)
    discount_total += global_discount_value

    grand_total = subtotal - discount_total + tax_total

    invoice = {
        "customer_name": bill["customer"]["name"],
        "customer_phone": bill["customer"].get("phone"),
        "subtotal": round(subtotal, 2),
        "discount_total": round(discount_total, 2),
        "tax_total": round(tax_total, 2),
        "grand_total": round(grand_total, 2),
        "global_discount_pct": round(global_pct, 2),
        "items": items_out
    }
    return invoice


def persist_invoice(conn, invoice: dict, notes: str = None) -> str:
    invoice_no = "INV-" + datetime.now().strftime("%Y%m%d") + "-" + uuid.uuid4().hex[:6].upper()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO invoices
                    (invoice_no, customer_name, customer_phone, subtotal, discount_total, tax_total, grand_total, notes)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
                invoice_no, invoice["customer_name"], invoice.get("customer_phone"),
                invoice["subtotal"], invoice["discount_total"], invoice["tax_total"],
                invoice["grand_total"], notes
            ))
            cur.execute("SELECT LAST_INSERT_ID()")
            invoice_id = cur.fetchone()[0]

            for it in invoice["items"]:
                cur.execute("""
                        INSERT INTO invoice_items
                        (invoice_id, sku, name, qty, unit_price, discount_pct, tax_pct,
                         line_subtotal, line_discount, line_tax, line_total)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (
                    invoice_id, it["sku"], it["name"], it["qty"], it["unit_price"],
                    it["discount_pct"], it["tax_pct"], it["line_subtotal"],
                    it["line_discount"], it["line_tax"], it["line_total"]
                ))

        conn.commit()
        log(f"Saved invoice {invoice_no} (ID {invoice_id}) to MySQL.")
        return invoice_no
    except Exception as e:
        conn.rollback()
        raise


def export_invoice_csv(invoice: dict, invoice_no: str):
    header = pd.DataFrame([{
        "invoice_no": invoice_no,
        "customer_name": invoice["customer_name"],
        "customer_phone": invoice.get("customer_phone"),
        "subtotal": invoice["subtotal"],
        "discount_total": invoice["discount_total"],
        "tax_total": invoice["tax_total"],
        "grand_total": invoice["grand_total"],
        "global_discount_pct": invoice.get("global_discount_pct", 0.0)
    }])
    items = pd.DataFrame(invoice["items"])

    header_path = os.path.join(BASE_DIR, f"{invoice_no}_header.csv")
    items_path = os.path.join(BASE_DIR, f"{invoice_no}_items.csv")

    header.to_csv(header_path, index=False, encoding="utf-8")
    items.to_csv(items_path, index=False, encoding="utf-8")

    log(f"Exported invoice CSVs:\n  {header_path}\n  {items_path}")


def main():
    log(f"Script directory: {BASE_DIR}")
    log(f"Catalog CSV path: {CATALOG_CSV}")
    log(f"Bill JSON path:   {BILL_JSON}")

    ensure_catalog_csv(CATALOG_CSV)
    ensure_bill_json(BILL_JSON)

    ensure_billing_db_and_tables()

    catalog = load_catalog(CATALOG_CSV)
    bill = load_bill(BILL_JSON)

    invoice = compute_invoice(catalog, bill)

    conn = connect_db()
    try:
        invoice_no = persist_invoice(conn, invoice, notes="Generated via m6_4_billing.py")
    finally:
        conn.close()
        log("MySQL connection closed.")

    export_invoice_csv(invoice, invoice_no)

    log("=== Final Invoice Summary ===")
    print(pd.DataFrame([{
        "invoice_no": invoice_no,
        "customer_name": invoice["customer_name"],
        "subtotal": invoice["subtotal"],
        "discount_total": invoice["discount_total"],
        "tax_total": invoice["tax_total"],
        "grand_total": invoice["grand_total"]
    }]).to_string(index=False))
    log("Done.")


if __name__ == "__main__":
    main()