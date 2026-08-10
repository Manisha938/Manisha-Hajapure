class Student:
  Studentcount=0
    
  def __init__(self,Rollno,Name,Marks):
    self.Rollno=Rollno
    self.Name=Name
    self.Marks=Marks
    Student.Studentcount+=1
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
    print(f"Rollno={self.Rollno}\t Name={self.Name} \t Marks={self.Marks} ")

class placedStudent(Student):
  def __init__(self,Rollno,name,marks,sal):
    super().__init__ (Rollno,name,marks)
    self.sal=sal
  def display(self):
    print(f"sal={self.sal}\t",end=" ")
    return super().display()
 
s3=placedStudent(12,"manisha",190,100000)        
s1=Student(101,"virat",90.20)
s2=Student(102,"virati",8.20)
print(Student.Studentcount)
s1.display()
s3.display()

    

     
        
    



    
    
    
