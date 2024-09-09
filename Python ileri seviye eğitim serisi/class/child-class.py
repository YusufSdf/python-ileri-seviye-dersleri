class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def intro(self):
        print(self.name,self.surname,self.age)


class Student(Person):
    def __init__(self, name, surname, age,number= 200):
        super().__init__(name, surname, age)
        # Person.__init__(self,name,surname,age)
        self.number = number
        print(self.number)

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age) 
        self.branch = branch
        print(self.branch)

s1 = Student("yusuf","sedef",19)

