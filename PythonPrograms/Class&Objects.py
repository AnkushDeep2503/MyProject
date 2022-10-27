class Calculator:
    num = 50

    def __init__(self, num1, num2):
        self.firstnum = num1
        self.secondnum = num2
        print("whatever")

    def myMethod(self):
        print("execute now for method")

    def methodValue(self):
        return self.firstnum + self.secondnum + self.num


obj = Calculator(3, 5)
print(obj.methodValue())
obj.myMethod()

obj1 = Calculator(4, 9)
obj1.myMethod()
print(obj1.methodValue())