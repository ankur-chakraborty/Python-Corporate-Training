class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        return NotImplemented

acc1 = BankAccount("A101", 2500)
acc2 = BankAccount("A102", 3200)

print(acc1 + acc2)
