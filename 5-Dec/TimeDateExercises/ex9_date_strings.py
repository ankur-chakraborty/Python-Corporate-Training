from datetime import datetime
def sort_dates(date_list):
    return sorted([datetime.strptime(d, "%Y-%m-%d") for d in date_list])
print(sort_dates(["2025-01-20", "2024-12-21", "2025-01-22"]))
