import pymysql
import pandas as pd

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "DipsuAnk2016"  # <-- update if needed
DB_NAME = "employee_app"


def connect_db():
    return pymysql.connect(
        host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD,
        database=DB_NAME, autocommit=True
    )


def add_employee():
    name = input("Name: ").strip()
    dept = input("Department: ").strip()
    role = input("Role: ").strip()
    salary = float(input("Salary: ").strip())
    email = input("Email: ").strip() or None
    phone = input("Phone: ").strip() or None
    hired_on = input("Hired On (YYYY-MM-DD, blank=today): ").strip() or None

    conn = connect_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO employees (name, dept, role, salary, email, phone, hired_on)
                VALUES (%s,%s,%s,%s,%s,%s, COALESCE(%s, CURRENT_DATE))
            """, (name, dept, role, salary, email, phone, hired_on))
        print("✅ Employee added.")
    finally:
        conn.close()


def view_all():
    conn = connect_db()
    try:
        df = pd.read_sql("SELECT * FROM employees ORDER BY emp_id", conn)
        print(df if not df.empty else "No employees found.")
    finally:
        conn.close()


def update_salary():
    emp_id = int(input("Employee ID: ").strip())
    new_salary = float(input("New Salary: ").strip())
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE employees SET salary=%s WHERE emp_id=%s", (new_salary, emp_id))
        print("✅ Salary updated.")
    finally:
        conn.close()


def delete_employee():
    emp_id = int(input("Employee ID to delete: ").strip())
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
        print("🗑️ Employee deleted (if existed).")
    finally:
        conn.close()


def search_by_name():
    keyword = input("Search keyword for name: ").strip()
    like = f"%{keyword}%"
    conn = connect_db()
    try:
        df = pd.read_sql("SELECT * FROM employees WHERE name LIKE %s", conn, params=[like])
        print(df if not df.empty else "No matches.")
    finally:
        conn.close()


def export_to_csv():
    filename = input("Output CSV filename (default employees.csv): ").strip() or "employees.csv"
    conn = connect_db()
    try:
        df = pd.read_sql("SELECT * FROM employees ORDER BY emp_id", conn)
        df.to_csv(filename, index=False)
        print(f"📄 Exported to {filename}")
    finally:
        conn.close()


def main_menu():
    while True:
        print("\n=== Employee Management ===")
        print("1) Add employee")
        print("2) View all")
        print("3) Update salary")
        print("4) Delete employee")
        print("5) Search by name")
        print("6) Export to CSV")
        print("0) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all()
        elif choice == "3":
            update_salary()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            export_to_csv()
        elif choice == "0":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main_menu()