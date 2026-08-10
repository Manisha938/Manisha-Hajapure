#Create a class Distance with data members as km,m and cm and add following
#methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator
class Distance:
    #constructor
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm

        #display
    def display(self):
        print(f"{self.km}\t {self.m}\t {self.cm} cm")

        #overload + operator
    def __add__(self,other):
        cm=self.cm + other.cm
        m=self.m + other.m
        km=self.km + other.km

#covert cm tom
        if cm>= 100:
            m +=cm //100
            cm=cm %100
            m =m %100

        #overlaod - operator
    def __sub__(self,other):
        cm1=(self.km*10000)+(self.m*100)+self.cm
        cm2=(other.km*10000)+(other.m*100)+other.cm

        diff=cm1 -cm2

        km=diff//1000000
        diff%= 10000
        m=diff//100
        cm=diff %100

        return Distance(km,m,cm)

    #destructor
    def __del__(self):
        print("distance object destoyed")

d1=Distance(2,500,60)
d2=Distance(1,7000,80)

print("----first distance-----")
d1.display()

print("----second  distance-----")   
d2.display()

d3=d1+d2
print("----addition:----")

d4=d1-d2
print("-----subtraction----")
d4.display()

