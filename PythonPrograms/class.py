class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(type(self.name))

    def MethodCalling(self):
        print("My name is", self.name, "and my age is", self.age)


obj = Person("Ankush", 34)
obj.MethodCalling()


class Student(Person):
    pass


obj1 = Student("Surbhi", 28)
obj1.MethodCalling()