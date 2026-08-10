#2. Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook
class Product:
    def __init__(self,pid,pname,quantity):
        self.pid=pid
        self.pname=pname
        self.quantity=quantity
        print("constructor calling:")

    def getpid(self):
        return self.pid
    def setpid(self,pid):
        self.pid=pid

    def getpname(self):
        return self.pname
    def setpname(self,pname):
        self.pname=pname

    def getquantity(self):
        return self.quantity
    def setquantity(self,quantity):
        self. quantity=quantity

    def display(self):
        print(f'pid={self.pid} \t pname={self.pname}\t quantity={self.quantity}') 
p1=Product(101,"laptop",10)
p1.display()
p2=Product(102,"mobile",20)
p2.display() 
p3=Product(103,"ipat",90)
p3.display()
p4=Product(104,"bycycle",40) 
p4.display()     

