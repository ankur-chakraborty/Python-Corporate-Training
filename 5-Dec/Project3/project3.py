import pymysql
import pandas as pd
from datetime import date, timedelta

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "DipsuAnk2016"  # update if needed
DB_NAME = "library_app"


def db():
    return pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD,
                           database=DB_NAME, autocommit=True)


def search_books():
    q = input("Search by title/author: ").strip()
    like = f"%{q}%"
    conn = db()
    try:
        df = pd.read_sql("""
            SELECT book_id, title, author, isbn, copies_available
            FROM books
            WHERE title LIKE %s OR author LIKE %s
            ORDER BY title
        """, conn, params=[like, like])
        print(df if not df.empty else "No matches.")
    finally:
        conn.close()


def borrow_book():
    member_id = int(input("Member ID: ").strip())
    book_id = int(input("Book ID: ").strip())
    days = int(input("Days to borrow (default 14): ").strip() or "14")
    due = date.today() + timedelta(days=days)

    conn = db()
    try:
        with conn.cursor() as cur:
            # Check availability
            cur.execute("SELECT copies_available FROM books WHERE book_id=%s", (book_id,))
            row = cur.fetchone()
            if not row:
                print("❌ Book not found.");
                return
            if row[0] <= 0:
                print("❌ No copies available.");
                return

            # Create borrow + decrement
            cur.execute("""
                INSERT INTO borrows (member_id, book_id, due_date, status)
                VALUES (%s, %s, %s, 'Borrowed')
            """, (member_id, book_id, due))
            cur.execute("UPDATE books SET copies_available = copies_available - 1 WHERE book_id=%s", (book_id,))
        print(f"✅ Borrow created. Due on {due}")
    finally:
        conn.close()


def return_book():
    borrow_id = int(input("Borrow ID: ").strip())
    conn = db()
    try:
        with conn.cursor() as cur:
            # Check borrow
            cur.execute("SELECT book_id, status FROM borrows WHERE borrow_id=%s", (borrow_id,))
            row = cur.fetchone()
            if not row:
                print("❌ Borrow not found.");
                return
            book_id, status = row
            if status == "Returned":
                print("ℹ️ Already returned.");
                return

            # Mark returned + increment copies
            cur.execute("UPDATE borrows SET status='Returned', return_date=CURRENT_DATE WHERE borrow_id=%s",
                        (borrow_id,))
            cur.execute("UPDATE books SET copies_available = copies_available + 1 WHERE book_id=%s", (book_id,))
        print("✅ Book returned.")
    finally:
        conn.close()


def list_borrows():
    conn = db()
    try:
        df = pd.read_sql("""
            SELECT b.borrow_id, m.name AS member, k.title AS book, b.borrow_date, b.due_date, b.return_date, b.status
            FROM borrows b
            JOIN members m ON b.member_id = m.member_id
            JOIN books   k ON b.book_id   = k.book_id
            ORDER BY b.borrow_id DESC
        """, conn)
        print(df if not df.empty else "No borrow records.")
    finally:
        conn.close()


def menu():
    while True:
        print("\n=== Library CLI ===")
        print("1) Search books")
        print("2) Borrow book")
        print("3) Return book")
        print("4) List borrows")
        print("0) Exit")
        c = input("Choose: ").strip()
        if c == "1":
            search_books()
        elif c == "2":
            borrow_book()
        elif c == "3":
            return_book()
        elif c == "4":
            list_borrows()
        elif c == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()