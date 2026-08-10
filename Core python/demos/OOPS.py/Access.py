#constrator
class Emp:
  def __init__(self,id,name,sal):
    self.__id=id
    self.__sal=sal
    self.__name=name
  def getid(self):
    return self.__id
  def setid(self,id):
    self.__id=id
  def getname(self):
    return self.__name
  def setname(self,name):
    self.__name=name
  def getsal(self):
    return self.__sal
  def setsal(self,sal):
    self.__sal=sal
  def calsal(self):
    print(f"Emp salay ={self.sal}")
  def display(self):
   print(f'id={self.__id}\t name={self.__name} \t sal={self.__sal}')

class Hr(Emp):
  def __init__(self,id,name,sal,com=150):
    super().__init__(id,name,sal)
    self.__com=com
  def getCom(self):
    return self.__com
  def setcom(self,com):
    self.__com=com
  def display(self):
    print(f"com={self.__com}",end="\t")
    super().display()
  def __del__(self):
    print("distructor is called")
h1=Hr(212,"sumit",3213)
h1.display()
e1=Emp(120,"manisha",1000)
e1.display()
