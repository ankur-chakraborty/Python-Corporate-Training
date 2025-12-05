import os
import sys
from datetime import datetime
import pandas as pd
import pymysql

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Aayyuusshhii@01"
DB_NAME = "retail_app"
ORDERS_TABLE = "orders"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_CSV = os.path.join(BASE_DIR, "products.csv")
OUTPUT_EXCEL = os.path.join(BASE_DIR, "retail_report.xlsx")
ALLOW_SYNTHETIC_ORDERS_IF_EMPTY = True


def log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {msg}")

def ensure_products_csv(csv_path: str = PRODUCTS_CSV):
    if os.path.exists(csv_path):
        log(f"Found products CSV: {os.path.abspath(csv_path)}")
        return
    log("products.csv not found. Creating default catalog...")

    data = [
        {"sku": "SKU-101", "product_name": "Wireless Mouse",        "category": "Accessories", "unit_cost": 180,  "default_price": 499},
        {"sku": "SKU-102", "product_name": "Mechanical Keyboard",   "category": "Accessories", "unit_cost": 900,  "default_price": 1399},
        {"sku": "SKU-103", "product_name": "USB-C Cable",           "category": "Accessories", "unit_cost": 60,   "default_price": 199},
        {"sku": "SKU-104", "product_name": '27" Monitor',           "category": "Displays",    "unit_cost": 2000, "default_price": 2999},
        {"sku": "SKU-105", "product_name": "Laptop Stand",          "category": "Accessories", "unit_cost": 250,  "default_price": 799},
        {"sku": "SKU-106", "product_name": "Webcam 1080p",          "category": "Accessories", "unit_cost": 700,  "default_price": 1499},
    ]
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False, encoding="utf-8")
    log(f"Created products.csv at: {os.path.abspath(csv_path)}")

def connect_db():
    log(f"Connecting to MySQL at {MYSQL_HOST} with user '{MYSQL_USER}', DB '{DB_NAME}'...")
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=DB_NAME,
        autocommit=True
    )

    with conn.cursor() as cur:
        cur.execute("SELECT DATABASE()")
        db_name = cur.fetchone()[0]
        log(f"Connected to DB: {db_name}")
        cur.execute(f"SHOW TABLES LIKE %s", (ORDERS_TABLE,))
        exists = cur.fetchone() is not None
        log(f"Orders table exists: {exists}")
        if not exists:

            log(f"Creating table '{ORDERS_TABLE}' (not found).")

            cur.execute(f"""

                CREATE TABLE {ORDERS_TABLE} (

                  order_id INT PRIMARY KEY,

                  order_date DATE NOT NULL,

                  customer_id INT NOT NULL,

                  customer_name VARCHAR(120) NOT NULL,

                  sku VARCHAR(50) NOT NULL,

                  quantity INT NOT NULL,

                  unit_price DECIMAL(10,2) NOT NULL

                )

            """)

            log("Created orders table.")

    return conn


def seed_orders_if_empty(conn):

    with conn.cursor() as cur:

        cur.execute(f"SELECT COUNT(*) FROM {ORDERS_TABLE}")

        count = cur.fetchone()[0]

        log(f"Current orders row count: {count}")

        if count == 0 and ALLOW_SYNTHETIC_ORDERS_IF_EMPTY:

            log("Seeding synthetic orders for testing...")

            rows = [

                (1001, '2025-11-28', 1, 'Rahul Sharma', 'SKU-101', 2, 499.00),

                (1002, '2025-11-29', 2, 'Aisha Khan',   'SKU-102', 1, 1299.00),

                (1003, '2025-12-01', 2, 'Aisha Khan',   'SKU-101', 3, 459.00),

                (1004, '2025-12-03', 3, 'Ravi Kumar',   'SKU-103', 5, 199.00),

                (1005, '2025-12-03', 4, 'Meera Iyer',   'SKU-104', 1, 2999.00),

            ]

            cur.executemany(f"""

                INSERT INTO {ORDERS_TABLE}

                (order_id, order_date, customer_id, customer_name, sku, quantity, unit_price)

                VALUES (%s,%s,%s,%s,%s,%s,%s)

            """, rows)

            log("Seeded orders table with 5 rows.")


def load_orders(conn) -> pd.DataFrame:

    sql = f"""

        SELECT order_id, order_date, customer_id, customer_name, sku, quantity, unit_price

        FROM {ORDERS_TABLE}

    """

    df = pd.read_sql(sql, conn)

    log(f"Loaded orders: {len(df)} rows")

    if df.empty:

        return df

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)

    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0.0)

    df["sku"] = df["sku"].astype(str)

    df = df.dropna(subset=["order_date", "customer_id", "customer_name", "sku"])

    return df





def load_products(csv_path: str) -> pd.DataFrame:

    log(f"Loading products CSV from: {os.path.abspath(csv_path)}")

    df = pd.read_csv(csv_path)

    log(f"Loaded products: {len(df)} rows")

    required = {"sku", "product_name", "category", "unit_cost"}

    missing = required - set(df.columns)

    if missing:

        raise ValueError(f"Products CSV missing required columns: {missing}")

    df["sku"] = df["sku"].astype(str)

    df["unit_cost"] = pd.to_numeric(df["unit_cost"], errors="coerce").fillna(0.0)

    if "default_price" in df.columns:

        df["default_price"] = pd.to_numeric(df["default_price"], errors="coerce").fillna(0.0)

    return df


def merge_and_compute(orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:

    merged = orders.merge(products, on="sku", how="left", validate="m:1")


    unknown_mask = merged["product_name"].isna()

    if unknown_mask.any():

        unknown_skus = merged.loc[unknown_mask, "sku"].unique().tolist()

        log(f"WARNING: {unknown_mask.sum()} order lines with unknown SKU(s): {unknown_skus}")

        merged["product_name"] = merged["product_name"].fillna("UNKNOWN")

        merged["category"] = merged["category"].fillna("UNKNOWN")

        merged["unit_cost"] = merged["unit_cost"].fillna(0.0)

    merged["line_revenue"] = merged["quantity"] * merged["unit_price"]

    merged["line_cost"] = merged["quantity"] * merged["unit_cost"]

    merged["line_margin"] = merged["line_revenue"] - merged["line_cost"]

    merged["order_month"] = merged["order_date"].dt.to_period("M").astype(str)

    merged = merged.sort_values(["order_date", "order_id", "sku"]).reset_index(drop=True)

    log(f"Merged rows: {len(merged)}")

    return merged


def build_dashboards(merged: pd.DataFrame):

    total_orders = int(merged["order_id"].nunique())

    total_units = int(merged["quantity"].sum())

    total_revenue = float(merged["line_revenue"].sum())

    total_margin = float(merged["line_margin"].sum())

    avg_order_value = float(merged.groupby("order_id")["line_revenue"].sum().mean() or 0.0)

    summary_df = pd.DataFrame([

        {"Metric": "Report Generated At", "Value": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},

        {"Metric": "Total Orders", "Value": total_orders},

        {"Metric": "Total Units", "Value": total_units},

        {"Metric": "Total Revenue", "Value": round(total_revenue, 2)},

        {"Metric": "Total Margin", "Value": round(total_margin, 2)},

        {"Metric": "Average Order Value (AOV)", "Value": round(avg_order_value, 2)},

        {"Metric": "Output Excel Path", "Value": os.path.abspath(OUTPUT_EXCEL)},

    ])

    by_category = (

        merged.groupby("category", dropna=False)

        .agg(

            orders=("order_id", "nunique"),

            units=("quantity", "sum"),

            revenue=("line_revenue", "sum"),

            cost=("line_cost", "sum"),

            margin=("line_margin", "sum"),

        )

        .reset_index()

        .sort_values("revenue", ascending=False)

    )


    by_month = (

        merged.groupby("order_month", dropna=False)

        .agg(

            orders=("order_id", "nunique"),

            units=("quantity", "sum"),

            revenue=("line_revenue", "sum"),

            cost=("line_cost", "sum"),

            margin=("line_margin", "sum"),

        )

        .reset_index()

        .sort_values("order_month")

    )


    top_customers = (

        merged.groupby(["customer_id", "customer_name"], dropna=False)

        .agg(

            orders=("order_id", "nunique"),

            units=("quantity", "sum"),

            revenue=("line_revenue", "sum"),

            margin=("line_margin", "sum"),

        )

        .reset_index()

        .sort_values("revenue", ascending=False)

        .head(5)

    )


    top_products = (

        merged.groupby(["sku", "product_name"], dropna=False)

        .agg(

            orders=("order_id", "nunique"),

            units=("quantity", "sum"),

            revenue=("line_revenue", "sum"),

            margin=("line_margin", "sum"),

        )

        .reset_index()

        .sort_values("revenue", ascending=False)

        .head(10)

    )

    return {

        "Summary": summary_df,

        "OrderLinesMerged": merged,

        "ByCategory": by_category,

        "ByMonth": by_month,

        "TopCustomers": top_customers,

        "TopProducts": top_products,

    }


def export_to_excel(tables: dict, out_path: str):

    log(f"Exporting Excel to: {os.path.abspath(out_path)}")

    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:

        for sheet_name, df in tables.items():

            df_out = df.copy()

            num_cols = df_out.select_dtypes(include=["float", "int"]).columns

            for col in num_cols:

                if col not in ("orders", "units"):

                    df_out[col] = pd.to_numeric(df_out[col], errors="coerce").astype(float).round(2)

            df_out.to_excel(writer, index=False, sheet_name=sheet_name)

    log("Excel export complete.")


def main():

    log(f"Script location: {BASE_DIR}")

    log(f"Expecting products CSV here: {PRODUCTS_CSV}")

    log(f"Will write Excel report here: {OUTPUT_EXCEL}")

    try:

        ensure_products_csv(PRODUCTS_CSV)


        conn = connect_db()

        seed_orders_if_empty(conn)


        orders = load_orders(conn)

        if orders.empty:

            log("No orders found. Please insert rows into the orders table.")

            return


        products = load_products(PRODUCTS_CSV)


        merged = merge_and_compute(orders, products)


        tables = build_dashboards(merged)


        export_to_excel(tables, OUTPUT_EXCEL)


        log("=== Summary (Console) ===")

        print(tables["Summary"].to_string(index=False))

        log("Top 5 Customers:")

        print(tables["TopCustomers"].to_string(index=False))

        log("Done.")

    except Exception as e:

        print("❌ Error:", e, file=sys.stderr)

    finally:

        try:

            conn.close()

            log("MySQL connection closed.")

        except Exception:

            pass


if __name__ == "__main__":

    main()
