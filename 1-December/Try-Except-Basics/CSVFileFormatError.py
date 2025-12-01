import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if not rows or not all(isinstance(row, list) for row in rows):
                raise ValueError("Invalid CSV format.")
            print("CSV content:")
            for row in rows:
                print(row)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_path1 = "data.csv"
read_csv(file_path1)
