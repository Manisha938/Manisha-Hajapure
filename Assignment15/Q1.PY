#Create a class Book with members as bid,bname,price and author.Add following
#methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#constrator
class Book:
  def __init__(self,bid,bname,price,author):
    self.bid=bid
    self.bname=bname
    self.price=price
    self.author=author
    print("Constructor calling:")
  def getbid(self):
    return self.bid
  def setid(self,bid):
    self.bid=bid
  def getbname(self):
    return self.bname
  def setname(self,bname):
    self.bname=bname
  def getprice(self):
    return self.price
  def setprice(self,price):
    self.price=price
  def getauthor(self):
    return self.author
  def setauthor(self,author):
    self.author=author

  def display(self):
   print(f'bid={self.bid}\t bname={self.bname} \t price={self.price} \t author={self.author}')
e1=Book(101,"english",1000,"vishal jadhav")
e1.display()
e2=Book(102,"shamchi aai",5000,"manisha hajapure")
e2.display()
e3=Book(103,"marathi",3000,"sakshi raut")
e3.display()
e4=Book(104,"math",500,"hande kapil")
e4.display()