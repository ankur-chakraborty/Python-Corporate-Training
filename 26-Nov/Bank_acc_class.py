class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance=self.balance+amount
        print("Deposited: ",amount)

    def withdraw(self, amount):
        self.balance=self.balance-amount
        print("Withdraw: ",amount)

    def checkBal(self):
        print(self.balance)

a1= BankAccount("A1", 10000)
a1.deposit(50000)
a1.checkBal()
a1.withdraw(35000)
a1.checkBal()
