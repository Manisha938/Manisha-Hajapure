
#heirachical inheritancclass Animal:
class Animal:
    def __init__(self,name,col,age):
        self.name=name
        self.color=col
        self.age=age
    def display(self):
        print(f"name={self.name}\t col={self.color}\t age={self.age}")

class Dog(Animal):
    def bark(self):
        print("dog is barking")
    


class Cat(Animal):
  def meow(self):
    print("cat is meowing")

d1=Dog("Rani","Black",3) 
d1.display()
d1.bark()

c1=Cat("mani","Gray",2)
c1.display()
c1.meow()