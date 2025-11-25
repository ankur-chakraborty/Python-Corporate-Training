data = (1, 2, 3, 4, 5)
is_increasing = True
for i in range(1, len(data)):
    if data[i] <= data[i - 1]:
        is_increasing = False
        break
if is_increasing:
    print("The tuple is strictly increasing.")
else:
    print("The tuple is NOT strictly increasing.")
