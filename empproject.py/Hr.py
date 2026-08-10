from Emp import Emp
class Hr(Emp):
    def __init__(self,EmpId,name,sal,com):
        super ().__init__(EmpId,name,sal)
        self.com=com
    def calsal(self):
        print(f"final sal of Hr={self.sal+self.com}")
    def __str__(self):
        return super().__str__()+f"\t com={self.com}"
    def __repr__(self):
        return self.__str__()