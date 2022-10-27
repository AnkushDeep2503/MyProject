class Calculator:
    intValue = 30 #property

    def __init__(self, a, b): #parametrized constructor
        self.var1 = a
        self.var2 = b
        print("Constructor is being called")

    def randomNumber(self): #function inside a class is called method
        print("This is called method because it is being called inside the class")

    def product(self):
        return self.var1 * self.var2 * Calculator.intValue


obj = Calculator(4, 3)
obj.randomNumber()
print(obj.intValue)
print(obj.product())
