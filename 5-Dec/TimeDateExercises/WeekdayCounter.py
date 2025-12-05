from datetime import date, timedelta



def count_weekdays(start, end):
    cnt = 0
    curr=start
    while curr<=end:
        if curr.weekday() <5:
            cnt+=1
        curr+=timedelta(days=1)
    return cnt



start_date=date(2025,12,20)
end_date=date(2025,12,22)

print(count_weekdays(start_date, end_date))


# def count_weekdays(start_date, end_date):
#
#     weekday_count = 0
#     current_date = start_date
#
#     while current_date <= end_date:
#         if current_date.weekday() < 5:  # Monday=0, Sunday=6
#             weekday_count += 1
#         current_date += timedelta(days=1)
#
#     return weekday_count
#
# start = date(2025, 12, 1)
# end = date(2025, 12, 10)
# print(count_weekdays(start, end))





