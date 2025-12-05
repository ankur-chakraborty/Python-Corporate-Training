class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Processing payment of ₹{self.amount}")


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process_payment(self):
        print(f"Credit Card Payment of ₹{self.amount} using card ending with {self.card_number[-4:]}")


class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process_payment(self):
        print(f"UPI Payment of {self.amount} using UPI ID {self.upi_id}")




cc = CreditCardPayment(1500, "4111111111111111")
cc.process_payment()

upi = UPIPayment(999, "ankur@upi")
upi.process_payment()
