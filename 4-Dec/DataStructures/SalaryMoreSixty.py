def filter_by_salary(employees, threshold=60000):
    """
    Supports:
    - {'Alice': 75000, 'Bob': 58000}
    - {'Alice': {'salary': 75000}, 'Bob': {'salary': 58000}}
    """
    result = {}
    for k, v in employees.items():
        if isinstance(v, dict):
            sal = v.get("salary")
            if isinstance(sal, (int, float)) and sal > threshold:
                result[k] = v
        elif isinstance(v, (int, float)) and v > threshold:
            result[k] = v
    return result

emp1 = {"Alice": 75000, "Bob": 58000, "Ira": 61000}
emp2 = {"Alice": {"salary": 75000, "dept": "IT"},
        "Bob": {"salary": 58000, "dept": "HR"},
        "Ira": {"salary": 61000, "dept": "Ops"}}

print(filter_by_salary(emp1))
print(filter_by_salary(emp2))
