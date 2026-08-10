#1. Create a class Book with members as bid,bname,price and author.Add following
##methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.

class Book:
    #static variable
    count=0
    #constructor
    def __init__(self,bid=101,bname="english",price=230,author="vishal patil"):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
         #object count increase
        Book.count=Book.count+1
    def getbid(self):
        return self.bid
    def setbid(self,bid):
        self.bid=bid
        
    def getbname(self):
        return self.bname
    def setbname(self,bname):
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
        print(f"bid={self.bid}\t bname={self.bname}\t price={self.price}\t author={self.author}")

#distructor
    def __del__(self):
        print("\n book object destroyed")

#parameterless constructor
b1=Book() 
#parameterized constructor
b2=Book(101,"python",500,"Geido")  

b1.display()
b2.display()

print("\n total book objects:",Book.count)