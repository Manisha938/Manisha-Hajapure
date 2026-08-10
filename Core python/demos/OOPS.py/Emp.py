#constrator
class Emp:
  def __init__(self,id,name,sal):
    self.id=id
    self.sal=sal
    self.name=name
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
  def __init__(self,id,name,sal,Com=150):
    super().__init__(id,name,sal)
    self.Com=Com
  def getCom(self):
    return self.com
  def setcom(self,com):
    self.com=com
  def display(self):
    print(f"Com={self.Com}",end="\t")
    return super().display()
  def __del__(self):
    print("distructor is called")
h1=Hr(212,"sumit",3213)
h1.display()
e1=Emp(101,"manisha",10000)
e2=Emp(102,"sakshi",50000)
e3=Emp(103,"vishal",300000)
e4=Emp(104,"china",500000)
print(h1.getname())
print(h1.getsal())






 




    
   


