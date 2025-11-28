import os


def generate_email_templates(input_file="names.txt", output_folder="emails"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, "r") as file:
        names = [line.strip() for line in file if line.strip()]

    for name in names:
        email_content = (
            f"Dear {name},\n\n"
            "Your training session starts tomorrow.\n\n"
            "Regards,\n"
            "Training Team"
        )
        file_path = os.path.join(output_folder, f"{name.replace(' ', '_')}_email.txt")
        with open(file_path, "w") as email_file:
            email_file.write(email_content)

    print(f"Emails generated successfully in '{output_folder}' folder.")


with open("names.txt", "w") as f:
    f.write("Alice\nBob\nCharlie\nDiana\nEthan\n")

generate_email_templates()