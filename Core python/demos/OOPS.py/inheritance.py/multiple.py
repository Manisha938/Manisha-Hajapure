#multiple inheritancclass Animal:
class Animal:
    def __init__(self,name,col,age):
        self.name=name
        self.color=col
        self.age=age
    def display(self):
        print(f"name={self.name}\t col={self.color}\t age={self.age}")

class Dog:
    def Dog_sound(self):
        print("dog is barking")
    


class Cat(Animal,Dog):
    def __init__(self,name, col,age,):
        Animal.__init__(self,name,col,age)

c1=Cat("Mani","gray",2)
c1.display()
c1.Dog_sound()