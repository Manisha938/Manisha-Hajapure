#Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook

#constrator
class Shirt:
  def __init__(self,sid,sname,type,price,size):
    self.sid=sid
    self.sname=sname
    self.type=type
    self.price=price
    self.size=size
    print("Constructor calling:")
  def getsid(self):
    return self.sid
  def setid(self,sid):
    self.sid=sid
  def getbsname(self):
    return self.sname
  def setsname(self,sname):
    self.sname=sname
  def gettype(self):
    return self.type
  def settype(self,sname):
    self.type=type
  def getprice(self):
    return self.price
  def setprice(self,price):
    self.price=price
  def getsize(self):
    return self.size
  def setsize(self,size):
    self.size=size

  def display(self):
   print(f'sid:{self.sid}\t sname={self.sname} \t type:{self.type}\t  price={self.price} \t size={self.size}')
s1=Shirt(101,"cotton shirt","formal",1200, "large")
s1.display()
s2=Shirt(102,"silver","polo shirt",1300,"midium")
s2.display()
s3=Shirt(103,"cotton","tshirt",3000,"small")
s3.display()
s4=Shirt(104,"cotton","formal",3400,"large")
s4.display()