from datetime import datetime, date
def check_date_status(given_date):
    d = datetime.strptime(given_date, '%Y-%m-%d').date()
    today = date.today()

    if d < today:
        return "past"
    elif d > today:
        return "future"
    else:
        return "today"
print(check_date_status("2025-12-05"))