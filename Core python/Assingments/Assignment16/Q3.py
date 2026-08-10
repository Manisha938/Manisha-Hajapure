#Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowBook
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and

    #static variable
class Shirt:
    size_price={"small":10, "medium":20,"large":30,"xlarge":50}
    
    #constructor
    def __init__(self,sid,sname,type,price,size,):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size
      
    def getsid(self):
        return self.sid
    def setbid(self,sid):
        self.sid=sid
        
    def getsname(self):
        return self.sname
    def setbname(self,sname):
        self.sname=sname

           
    def gettype(self):
        return self.type
    def settype(self,type):
        self.type=type
            
    def getprice(self):
        return self.price
    def setprice(self,price):
        self.price=price

            
    def getsize(self):
        return self.size
    def setsize(self,size):
        self.size=size

    
    def get_price(self):
        increase = Shirt.size_price.get(self.size, 0)
        return self.price + (self.price * increase / 100)
    
     #disply method   
    def display(self):
        final_prise=self.get_price()
        print("\n----shirt deatails-----")
        print(f" sid={self.sid}\t sname={self.sname}\t type={self.type}\t price={self.price}\t size={self.size}")
    
    
    def __del__(self):

        print("\n shirt object destroyed")



#parameterless constructor
s1=Shirt(101,"paymond","formal",1000,"medium") 
#parameterized constructor
s2=Shirt(101,"tshirt","formal",1000,"large")  

s1.display()
s2.display()
