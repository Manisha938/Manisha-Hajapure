#abstract class
from abc import ABC,abstractmethod
class Vehical(ABC):
    def __init__(self,name,color,price):
        self.__name=name
        self.__color=color
        self.__price=price
    @abstractmethod
    def breack(self):
        pass
    def __str__(self):
        return f"name={self.__name}\t color={self.__color}\t price={self.__price}"
class Car(Vehical):
    def __init__(self,name,color,price,sBealt):
        super().__init__(name,color,price)
        self.__seatbelt =sBealt
    def breack(self):
        print("this is the drump breack of Car")

    def __str__(self):
        return super().__str__()+ f"\t seatbelt={self.__seatbelt}"
v=Car("BMW","Black",12000000,6)
v.breack()
print(v)