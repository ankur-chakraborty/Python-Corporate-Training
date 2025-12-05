import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Conversion complete! JSON saved to '{json_file}'.")

csv_to_json("employees.csv", "employees.json")
