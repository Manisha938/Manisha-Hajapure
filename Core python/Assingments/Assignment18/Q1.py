#Create a class Complex Number with data members as real and imag and add
#following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def display(self):
        print(f"{self.real}+ {self.imag}i")


        #overloading+opertor
    def __add__(self,other):
        r=self.real + other.real
        i=self.imag + other.imag
        return Complex(r,i)

        #distructor
    def __del__(self):
        print("complex object destroyed")

    #main program
c1=Complex(4,5)
c2=Complex(2,3)

print("frist complex number:")
c1.display()

print("second complex number:")
c2.display()

c3=c1+c2
print("Addintion:")
c3.display()


