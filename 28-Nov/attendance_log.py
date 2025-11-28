import datetime

def log_attendance(student_name, status):
    if status not in ['Present', 'Absent']:
        print("Invalid status. Please use 'Present' or 'Absent'.")
        return
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"{timestamp}, {student_name}, {status}\n"

    with open("attendance.log", "a") as file:
        file.write(log_entry)

    print(f"Attendance logged for {student_name}: {status}")

students = [
    {"name": "Alice", "status": "Present"},
    {"name": "Bob", "status": "Absent"}
]

for student in students:
    log_attendance(student["name"], student["status"])