def unique_prices_in_order(price):
    return list(dict.fromkeys(price))


prices = [199, 99, 299, 199, 99, 499]
print(unique_prices_in_order(prices))
