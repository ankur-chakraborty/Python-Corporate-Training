from datetime import date, datetime
def calculate_age(dob):
    dob = datetime.strptime(dob, '%Y-%m-%d').date()
    today = date.today()

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12
    return years, months, days
print(calculate_age("2003-05-10"))