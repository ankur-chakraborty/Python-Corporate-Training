
from datetime import datetime, timedelta, date

def expiring_within_15_days(expiry_dates):

    today = date.today()
    limit = today + timedelta(days=15)
    result = []
    for d in expiry_dates:
        dt = datetime.strptime(d, '%Y-%m-%d').date()
        if today <= dt <= limit:
            result.append(d)
    return result


print(expiring_within_15_days(["2025-12-10", "2025-12-25", "2026-01-01"]))

