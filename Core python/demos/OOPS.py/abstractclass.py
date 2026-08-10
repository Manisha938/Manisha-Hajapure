#Abstract class
from abc import ABC,abstractclassmethod
class Emp(ABC):
  def __init__(self,id,name,sal):
    self.id=id
    self.sal=sal
    self.name=name
  @abstractclassmethod   
  def calSal(self):
    pass
  def getid(self):
    return self.id
  def setid(self,id):
    self.id=id
  def getname(self):
    return self.name
  def setname(self,name):
    self.name=name
  def getsal(self):
    return self.sal
  def setsal(self,sal):
    self.sal=sal
  def calsal(self):
    print(f"Emp salay ={self.sal}")
  def display(self):
   print(f'id={self.id}\t name={self.name} \t sal={self.sal}')

class Hr(Emp):
    def __init__(self,id,name,sal,com):
        super().__init__(self,id, name,sal,com)
        self.__com=com
    def calSal(self):
        finialSal=self.getSal()+self.__com
        print(f"final salary={finialSal}")


#e1=Emp(12,"manisha",10000)
#e1.display()
h1=Hr(12,"manisha",15000,121)
h1.display()
h1.calSal()
