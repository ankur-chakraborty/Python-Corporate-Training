import datetime


def log_error(message):
    """Logs an error message with a timestamp into error.log"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {message}\n"
    with open("error.log", "a") as file:
        file.write(log_entry)

for i in range(1, 6):
    log_error(f"Simulated error #{i}")
