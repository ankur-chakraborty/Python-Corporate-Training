from datetime import datetime


def count_mondays(timestamps):
    count = 0
    for ts in timestamps:
        if isinstance(ts, str):
            ts = ts.replace('Z', '+00:00')
            try:
                dt = datetime.fromisoformat(ts)
            except ValueError:
                dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        else:
            dt = ts

        if dt.weekday() == 0:
            count += 1
    return count
data = [
    "2025-12-01T09:00:00",
    "2025-12-02T10:00:00",
    datetime(2025, 12, 8, 9, 0),
    "2025-12-06 12:00:00",
]
print(count_mondays(data))
