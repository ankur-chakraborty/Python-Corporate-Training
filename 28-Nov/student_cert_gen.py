def generate_certificate(student_name):
    certificate_content = f"""
           Certificate of Completion
    This is to certify that

           {student_name}

    has successfully completed the course with excellence.    
    """
    file_name = f"{student_name.replace(' ', '_')}_Certificate.txt"
    with open(file_name, "w") as cert_file:
        cert_file.write(certificate_content)
    print(f"Certificate generated for: {student_name}")


input_file = "welcome.txt"

with open(input_file, "r") as file:
    student_names = file.readlines()


for name in student_names:
    student_name = name.strip()
    if student_name:
        generate_certificate(student_name)
