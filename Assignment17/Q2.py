#2. Create a derived class from Student as EnggStudent with :
#a. Data members as :
#i. Branch
#ii. InternalMarks
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method
class Student:

    def __init__(self, sid, name, age, percentage):
        self.sid = sid
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        return "General Rank"


class EnggStudent(Student):

    def __init__(self, sid, name, age, percentage, branch, internalMarks):
        super().__init__(sid, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def calculateRank(self):
        total = self.percentage + self.internalMarks/10

        if total >= 80:
            return "Excellent"
        else:
            return "Good"

    def display(self):
        print("Student ID :", self.sid)
        print("Name :", self.name)
        print("Branch :", self.branch)
        print("Internal Marks :", self.internalMarks)
        print("Rank :", self.calculateRank())

    def __str__(self):
        return f"{self.sid} {self.name} {self.branch}"


e1 = EnggStudent(102, "Manisha", 21, 75, "Computer", 18)
e1.display()