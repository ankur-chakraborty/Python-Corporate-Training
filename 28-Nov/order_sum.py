def create_order_summary(output_file="order_summary.txt"):
    items = []
    total = 0

    for i in range(1, 4):
        print(f"Enter details for item {i}:")
        name = input("Item name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        cost = quantity * price
        total += cost
        items.append((name, quantity, price, cost))

    with open(output_file, "w") as file:
        file.write("ORDER SUMMARY\n\n")
        file.write(f"{'Item':<15}{'Qty':>5}{'Price':>10}{'Cost':>10}\n")
        file.write("-" * 45 + "\n")
        for name, qty, price, cost in items:
            file.write(f"{name:<15}{qty:>5}{price:>10.2f}{cost:>10.2f}\n")
        file.write("-" * 45 + "\n")
        file.write(f"{'Total':<30}{total:>10.2f}\n")

    print(f"Order summary saved to {output_file}.")


create_order_summary()