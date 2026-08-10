from abc import ABC,abstractmethod
class Emp(ABC):
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    @abstractmethod
    def calsal():
        pass
    def __str__(self):
        return f"Id={self.Id}\t name={self.name}\t salary={self.sal}"
    def __repr__(self):
        return self.__str__()