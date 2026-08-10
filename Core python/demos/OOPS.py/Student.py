class Student:
  collageName="FBS"
  def __init__(self,Rollno,Name,Marks):
    self.Rollno=Rollno
    self.Name=Name
    self.Marks=Marks

  def getRollno(self):
    return self.Rollno
  def setRollno(self,Rollno):
    self.Rollno=Rollno

      
  def getName(self):
    return self.Name
  def setName(self,Name):
    self.Name=Name

      
  def getMarks(self):
    return self.Marks
  def setMarks(self,Marks):
    self.Marks=Marks

  def display(self):
    print(f"Rollno={self.Rollno}\t Name={self.Name} \t Marks={self.Marks} \t college Name={Student.collageName}")
s1=Student(101,"virat",90.20)
s1.display()
s2=Student(102,"virati",8.20)
s2.display()
print(Student.collageName)
Student.collegeName="Firstbit Solution"
print(Student.collegeName)

  


      



