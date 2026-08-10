#Create a class Student with following
#a. data members :
#i. StudentId
#ii. Name
#iii. Age
#iv. Percentage
##b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. Method CalculateRank
#v. Override __str__ Method
class Student:

    def __init__(self, sid, name, age, percentage):
        self.sid = sid
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Pass"

    def display(self):
        print("Student ID :", self.sid)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Percentage :", self.percentage)
        print("Rank :", self.calculateRank())

    def __str__(self):
        return f"{self.sid} {self.name} {self.age} {self.percentage}"


s1 = Student(101, "Manisha", 20, 82)
s1.display()