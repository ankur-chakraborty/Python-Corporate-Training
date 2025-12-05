import pymysql
import pandas as pd
from datetime import datetime, date
import sys

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "DipsuAnk2016"
DB_NAME = "subscription_app"
PRICE_MAP = {
    "Monthly": 1000,
    "Quarterly": 2700,
    "Yearly": 10000
}

def connect_server():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        autocommit=True
    )

def connect_db():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=DB_NAME,
        autocommit=True
    )

def setup_database():
    conn = connect_server()
    try:
        with conn.cursor() as cur:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        conn.select_db(DB_NAME)
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS subscriptions;")
            cur.execute("""
                CREATE TABLE subscriptions (
                  sub_id INT PRIMARY KEY,
                  customer_name VARCHAR(50) NOT NULL,
                  start_date DATE NOT NULL,
                  expiry_date DATE NOT NULL,
                  created_at DATETIME NOT NULL,
                  plan_type VARCHAR(20) NOT NULL
                );
            """)

            rows = [
                (1,  'Aisha Khan',   '2024-12-15', '2025-01-15', '2024-12-15 10:30:00', 'Monthly'),
                (2,  'Rahul Sharma', '2025-01-05', '2025-02-05', '2025-01-05 09:45:00', 'Monthly'),
                (3,  'Imran Ali',    '2025-02-10', '2025-03-10', '2025-02-10 14:12:00', 'Monthly'),
                (4,  'Meera Iyer',   '2025-03-01', '2025-04-01', '2025-03-01 17:05:00', 'Monthly'),
                (5,  'Sanjay Patel', '2025-02-20', '2025-05-21', '2025-02-20 13:00:00', 'Quarterly'),
                (6,  'Neha Gupta',   '2024-06-10', '2025-06-10', '2024-06-10 08:15:00', 'Yearly'),
                (7,  'Arjun Mehta',  '2025-11-25', '2025-12-25', '2025-11-25 11:00:00', 'Monthly'),
                (8,  'Priya Nair',   '2025-12-01', '2025-12-31', '2025-12-01 12:00:00', 'Monthly'),
                (9,  'Ravi Kumar',   '2025-11-30', '2025-12-07', '2025-11-30 09:00:00', 'Monthly'),
                (10, 'Sneha Roy',    '2025-01-10', '2026-01-10', '2025-01-10 08:00:00', 'Yearly'),
                (11, 'Vikram Singh', '2025-10-01', '2025-12-30', '2025-10-01 10:15:00', 'Quarterly'),
                (12, 'Kiran Das',    '2025-11-05', '2025-12-05', '2025-11-05 10:45:00', 'Monthly')
            ]
            cur.executemany("""
                INSERT INTO subscriptions (sub_id, customer_name, start_date, expiry_date, created_at, plan_type)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, rows)
    finally:
        conn.close()

def load_dataframe():
    conn = connect_db()
    try:
        df = pd.read_sql("SELECT * FROM subscriptions", conn)
        return df
    finally:
        conn.close()


def transform_dates_and_status(df: pd.DataFrame) -> pd.DataFrame:

    df["start_date"]  = pd.to_datetime(df["start_date"])
    df["expiry_date"] = pd.to_datetime(df["expiry_date"])
    df["created_at"]  = pd.to_datetime(df["created_at"])

    df["created_at"] = df["created_at"].dt.strftime("%d-%m-%Y %H:%M")

    today_ts = pd.Timestamp.today().normalize()

    df["days_left"] = (df["expiry_date"] - today_ts).dt.days
    df["age_days"]  = (today_ts - df["start_date"]).dt.days

    def status(row):
        if row["days_left"] < 0:
            return "Expired"
        elif row["days_left"] <= 7:
            return "ExpiringSoon"
        else:
            return "Active"

    df["status"] = df.apply(status, axis=1)

    df["days_overdue"] = df["days_left"].apply(lambda x: abs(x) if x < 0 else 0)

    df["next_billing_date"] = df["expiry_date"].dt.date

    billing_due_today = df[df["next_billing_date"] == date.today()]["customer_name"].tolist()

    return df, billing_due_today

def run_analytics(df: pd.DataFrame):
    print("\n--- Report 1: Status Counts (Active vs ExpiringSoon vs Expired) ---")
    print(df["status"].value_counts())

    print("\n--- Report 2: Subscriptions expiring this week (0–7 days left) ---")
    print(df[df["days_left"].between(0, 7)][["sub_id","customer_name","plan_type","expiry_date","days_left","status"]])

    print("\n--- Report 3: Overdue Subscriptions (Expired) ---")
    print(df[df["days_left"] < 0][["sub_id","customer_name","plan_type","expiry_date","days_left","days_overdue"]])

    df["renewal_value"] = df["plan_type"].map(PRICE_MAP)

    print("\n--- Report 4: Next 30-Day Revenue Forecast ---")
    forecast = df[df["days_left"].between(0, 30)]["renewal_value"].sum()
    print(f"Projected Revenue (next 30 days): {forecast}")

    print("\n--- Report 5: Renewal Reminder List (days_left <= 5) ---")
    reminder = df[df["days_left"] <= 5][["customer_name","plan_type","expiry_date","days_left"]]
    print(reminder)

    print("\n--- Report 6: Customer Lifetime (age_days) ---")
    print(df[["customer_name","age_days"]])

    print("\n--- Report 7: Group by plan_type ---")
    grouped = df.groupby("plan_type").agg(
        total_customers=("sub_id", "count"),
        average_age=("age_days", "mean"),
        expected_renewal_revenue=("renewal_value", "sum")
    ).reset_index()
    print(grouped)

    print("\n--- Report 8: Average subscription age (overall) ---")
    print(f"Average age (days): {df['age_days'].mean():.2f}")

    return {
        "forecast_30d": forecast,
        "reminder_df": reminder,
        "grouped_df": grouped
    }

def export_csv(df: pd.DataFrame, filename: str = "subscription_report.csv"):

    out = df.copy()

    if "expiry_date" in out.columns and pd.api.types.is_datetime64_any_dtype(out["expiry_date"]):
        out["expiry_date"] = out["expiry_date"].dt.strftime("%Y-%m-%d")
    if "start_date" in out.columns and pd.api.types.is_datetime64_any_dtype(out["start_date"]):
        out["start_date"] = out["start_date"].dt.strftime("%Y-%m-%d")

    out.to_csv(filename, index=False)
    print(f"\nCSV exported: {filename}")


def main():
    print("Setting up database and loading sample data...")
    setup_database()

    print("Extracting data into pandas DataFrame...")
    df = load_dataframe()
    print("\nRaw DataFrame:")
    print(df)

    print("\nTransforming dates and computing statuses...")
    df, billing_due_today = transform_dates_and_status(df)
    print("\nTransformed DataFrame (head):")
    print(df.head())

    print(f"\nCustomers with billing due TODAY ({date.today()}): {billing_due_today}")

    print("\nRunning analytics & business reports...")
    _ = run_analytics(df)

    print("\nExporting final DataFrame to CSV...")
    export_csv(df, "subscription_report.csv")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
