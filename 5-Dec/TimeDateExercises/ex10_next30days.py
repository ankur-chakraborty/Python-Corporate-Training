from datetime import date, timedelta
def next_30_dates():
    today = date.today()
    return[(today + timedelta(days=i)).isoformat() for i in range(30)]
print(next_30_dates())