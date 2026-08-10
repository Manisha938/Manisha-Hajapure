#metodoverriting 
class Student:
    def __init__(self,name,rollno,marks):
        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
    def __str__(self):
        return f"name={self.__name}\t rollno={self.__rollno}\t marks={self.__marks} "
s1=Student(22,"MANISHA",90)
print(s1)