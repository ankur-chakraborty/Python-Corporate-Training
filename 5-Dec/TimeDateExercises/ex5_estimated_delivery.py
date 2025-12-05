from datetime import datetime, timedelta
def estimated_delivery(delivery_date, days):
    d = datetime.strptime(delivery_date, "%Y-%m-%d")
    return(d + timedelta(days=days)).date()

print(estimated_delivery("2025-01-20", 8))