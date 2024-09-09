class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def intro(self):
        print(self.name,self.surname,self.age)


class Student(Person):
    pass 

class Teacher(Person):
    pass 


p1 = Person("yusuf","sedef",19)
s1 = Student("ilsu","sedef",1)
s1.intro()
p1.intro()
