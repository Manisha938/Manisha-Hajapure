#single inheritance
class Animal:
    def __init__(self,name,col,age):
        self.name=name
        self.color=col
        self.age=age
    def display(self):
        print(f"name={self.name}\t col={self.color}\t age={self.age}")

class Dog(Animal):
    def __init__(self,name, col,age,):
        super().__init__(name,col,age)

d1=Dog("rani","black",3)
d1.display()