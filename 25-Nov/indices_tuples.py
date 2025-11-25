data = (1, 2, 3, 2, 4, 2, 5)
value = 2
positions = []
for i in range(len(data)):
    if data[i] == value:
        positions.append(i)
print("Index positions:", positions)
