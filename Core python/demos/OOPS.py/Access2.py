class Student:
    def __init__(self,rollno,name,marks):
        self.rollno=rollno
        self._name=name                 #privete
        self.__marks=marks              #protected
    def display(self):
        print(f"rollno={self.rollno}  \t name={self._name}\t marks={self.__marks}")

class Enstudent(Student):
    def __init__(self,rollno,name,marks,cgpa):
        super().__init__(rollno,name,marks)
        self.__cgpa=cgpa
e=Enstudent(12,"manisha",50,9.50)
e.display()
print(f"rollno={e.rollno}")
print(f"name={e._name}")
print(f"marks={e._Student__marks}")