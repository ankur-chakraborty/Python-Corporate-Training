class BankAccount:
    def __init__(self, name, balance, account_number, currency, is_active):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.currency = currency
        self.is_active = is_active

    def deposit(self,amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self,amount):
        self.balance -= amount
        print("Withdrawed:", amount)
    def get_balance(self):
        return self.balance
    def display(self):
        print("Name:", self.name)
        print("Balance", self.balance)
        print("Account Number", self.account_number)
        print("Currency:", self.currency)
        print("Status:", self.is_active)

class SavingsAccount(BankAccount):
    def __init__(self, name, balance, account_number, currency, is_active,interest_rate):
        super().__init__(name,balance,account_number,currency,is_active)
        self.interest_rate=interest_rate

    def apply_interest(self,interest):
        self.balance += (interest/100)*self.balance

    def display(self):
        super().display()
        print("Savings Account Interest Rate:", self.interest_rate)



c2=SavingsAccount("Dipsu", 1000,100026, "INR", True, 10)

print(c2.display())
c2.apply_interest(100)
print(c2.display())




