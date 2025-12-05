#Given a customer’s subscription start date and duration (in days), compute expiry date.
from datetime import date, timedelta

start=date(2025,4,6)

end=start+timedelta(days=50)
print(end)


