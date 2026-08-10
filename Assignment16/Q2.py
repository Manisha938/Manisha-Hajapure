#2. Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowBook
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.

class Product:
    #static variable
    discount=10
    #constructor
    def __init__(self,pid=101,pname="laptop",price=50030,quantity="1"):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
         
    def getpid(self):
        return self.pid
    def setbid(self,pid):
        self.pid=pid
        
    def getpname(self):
        return self.pname
    def setpname(self,pname):
        self.pname=pname

            
    def getprice(self):
        return self.price
    def setprice(self,price):
        self.price=price

            
    def getquantity(self):
        return self.quantity
    def setquantity(self,quantity):
        self.quantity=quantity 

    def display(self):
        print(f"pid={self.pid}\t pname={self.pname}\t price={self.price}\t quantity={self.quantity} ")
        
    def applydiscount(self):
        discount_amount=self.price * Product.discount/100
        final_price=self.price- discount_amount
        print("discount:",Product.discount)
        print("discount amount:",discount_amount)
        print("price after discount:",final_price)

#distructor
    def __del__(self):
        print("\n product object destroyed")

#parameterless constructor
p1=Product() 
#parameterized constructor
p2=Product(101,"mobile",50000,2)  

p1.display()
p1.applydiscount()

p2.display()
p2.applydiscount()