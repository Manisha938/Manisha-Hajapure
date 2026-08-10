#3. Create a class MedicalStudent inherited from Student with following:

#i. Data members :Specialization
#ii. MarksOfInternship
#b. Add the following methods :
##i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Meth
class Student:

    def __init__(self, sid, name, age, percentage):
        self.sid = sid
        self.name = name
        self.age = age
        self.percentage = percentage


class MedicalStudent(Student):
    def __init__(self, sid, name, age, percentage,
                 specialization, internshipMarks):
        super().__init__(sid, name, age, percentage)
        self.specialization = specialization
        self.internshipMarks = internshipMarks

    def calculateRank(self):
        total = self.percentage + self.internshipMarks/10

        if total >= 85:
            return "Outstanding"
        else:
            return "Good"

    def display(self):
        print("Student ID :", self.sid)
        print("Name :", self.name)
        print("Specialization :", self.specialization)
        print("Internship Marks :", self.internshipMarks)
        print("Rank :", self.calculateRank())

    def __str__(self):
        return f"{self.sid} {self.name} {self.specialization}"


m1 = MedicalStudent(201, "manisha", 22, 80,"Cardiology", 20)
m1.display()