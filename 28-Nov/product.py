def generate_catalog(input_file, output_file):
    """Reads products and prices from input_file and writes a formatted catalog to output_file."""
    products = []

    with open(input_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                product = " ".join(parts[:-1])
                price = parts[-1]
                products.append((product, price))

    max_product_len = max(len(p[0]) for p in products)
    max_price_len = max(len(p[1]) for p in products)

    with open(output_file, "w") as file:
        header = f"{'Product'.ljust(max_product_len)} {'Price'.rjust(max_price_len)}\n"
        file.write(header)
        file.write("-" * (max_product_len + max_price_len + 1) + "\n")
        for product, price in products:
            file.write(f"{product.ljust(max_product_len)} {price.rjust(max_price_len)}\n")

generate_catalog("products.txt", "catalog.txt")
