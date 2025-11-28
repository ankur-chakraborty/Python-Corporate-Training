def write_emp_record(emp_id, name, salary):
    record = f"""
    Employee Record
    ID: {emp_id}
    Name: {name}
    Salary: {salary}
    """

    with open ("Emp.txt","w") as f:
        f.write(record)

write_emp_record(1041,"Ankur", 35223)

