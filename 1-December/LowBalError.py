class LowBalanceError(Exception):
    pass

def withdraw(amount, balance):
    if amount>balance:
        raise LowBalanceError("Insufficient funds")
    return balance-amount

print(withdraw(100, 100))