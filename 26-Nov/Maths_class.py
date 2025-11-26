class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b == 0:
            return "Not possible"
        else:
            return self.a/self.b

c =Calculator(5,7)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())