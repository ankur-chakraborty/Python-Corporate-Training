class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance -= amount
        else:
            print("You don't have enough money to withdraw")

    def getBalance(self):
        return self.__balance

acc=BankAccount("John",20000)

acc.deposit(100)
acc.withdraw(200)
print(acc.getBalance())

acc.__balance=50000
print(acc.getBalance())