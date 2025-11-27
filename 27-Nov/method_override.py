class Notification:
    def send(self, message):
        print("Sending message",message)

class EmailNotif(Notification):
    def send(self, message):
        print("Sending EMAIL",message)

class SMSNotif(Notification):
    def send(self, message):
        print("Sending SMS",message)


n1 = EmailNotif()
n1.send("Your order is sent")

n2=SMSNotif()
n2.send("YourOTP is 1603")



#Architect gives a basic uniform base to everyone to create and build uponm that

class Payment:
    def Pay(self):

class GooglePay(Payment):
    def Pay(self):

class PhonePay(Payment):
    def Pay(self):

class PayTM(Payment):
    def Pay(self):

