#4. Create a class College which has collection of students. Add the
#following methods :
#a. Parameteried constructor for number of students.
#b. AddStudent
#c. GetStudent
#d. RemoveStudent
#e. Override __str__ Method

class College:

    def __init__(self, size):
        self.students = []
        self.size = size

    def AddStudent(self, student):
        self.students.append(student)
    def GetStudent(self, sid):
        for s in self.students:
            if s["id"] == sid:
                return s

    def RemoveStudent(self, sid):
        for s in self.students:
            if s["id"] == sid:
                self.students.remove(s)

    def __str__(self):
        return str(self.students)


c1 = College(5)

c1.AddStudent({"id": 101, "name": "Kapil"})
c1.AddStudent({"id": 102, "name": "Rahul"})

print(c1)

print("Student Found:")
print(c1.GetStudent(101))

c1.RemoveStudent(102)

print("After Removal:")
print(c1)