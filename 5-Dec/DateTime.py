from datetime import datetime, date, time, timedelta

# today=date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
#
# now=datetime.now()
# print(now)
#
#
# dob=date(2003,3,16)
# print(dob)
#
# now=datetime.now()
# formatted=now.strftime("%d-%m-%Y %H:%M:%S")
# print(formatted)

today=date.today()
next_week=today + timedelta(days=7)
yesterday=today - timedelta(days=1)

print(yesterday)
print(next_week)


start=date(2024,1,1)
end=date(2024,12,31)

diff=end-start

print(diff.days)

dt=datetime.combine(date(2025,3,16),time(10,43))
print(dt)