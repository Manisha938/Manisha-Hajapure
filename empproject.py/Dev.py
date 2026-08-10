from Emp import Emp
class Dev(Emp):
    def __init__(self,id,name,sal,bonus):
        super ().__init__(id,name,sal)
        self.bonus=bonus
    def calsal(self):
        print(f"final sal of Hr={self.sal+self.com}")
    def __str__(self):
        return f"id={self.id}\t name={self.name}\t sal={self.sal}\t bonus={self.bonus}"
    def __repr__(self):
        return self.__str__()