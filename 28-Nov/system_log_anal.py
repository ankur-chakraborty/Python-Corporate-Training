def summarize_log(input_file="system.log", output_file="log_summary.txt"):
    error_count = 0
    warning_count = 0
    info_count = 0

    with open(input_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    with open(output_file, "w") as file:
        file.write("LOG SUMMARY\n")
        file.write("-" * 20 + "\n")
        file.write(f"ERROR lines: {error_count}\n")
        file.write(f"WARNING lines: {warning_count}\n")
        file.write(f"INFO lines: {info_count}\n")

    print(f"Summary written to {output_file}.")


with open("system.log", "w") as f:
    f.write("INFO System started\n")
    f.write("WARNING Low disk space\n")
    f.write("ERROR Failed to load module\n")
    f.write("INFO User logged in\n")
    f.write("ERROR Network timeout\n")

summarize_log()