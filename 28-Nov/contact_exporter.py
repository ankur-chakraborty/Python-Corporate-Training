import csv


def export_contacts(input_file="contacts.csv", output_file="contacts_export.txt"):
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        with open(output_file, "w") as out_file:
            for row in reader:
                name = row["name"]
                phone = row["phone"]
                out_file.write(f"Name: {name:<10} | Phone: {phone}\n")
    print(f"Contacts exported successfully to {output_file}.")


with open("contacts.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "phone"])
    writer.writeheader()
    writer.writerows([
        {"name": "Rahul", "phone": "9988776655"},
        {"name": "Aisha", "phone": "9123456789"},
        {"name": "John", "phone": "9876543210"}
    ])

export_contacts()