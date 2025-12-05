from datetime import datetime

def write_log(message, filename="logfile.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

    print("Log entry added.")

write_log("Application started")
write_log("User logged in")
write_log("Error: Invalid input")
