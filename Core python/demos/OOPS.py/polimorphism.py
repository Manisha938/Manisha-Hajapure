#polimorphism
class Emp:
    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal
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
        finalSal=self.__sal
        print(f"Emp salary={finalSal}")
    def display():
        print(f"id={self.__id} \t name={self.__name} \t sal={self.__sal}")
    def __str__(self):
        return f"id={self.__id} \t name={self.__name}\t sal={self.__sal}"

    
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
    #def calSal(self):
       # finalSal=self.getSal()+self.__sal + self.__com  
        #Aprint(f"final salary of Hr={finalSal}")
    def __str__(self):
        return super().__str__()+f"com={self.__com}"
    def __del__(self):
        print("distructor is called")



h1=Hr(18,"manisha",12344,500)
h1.calsal()


