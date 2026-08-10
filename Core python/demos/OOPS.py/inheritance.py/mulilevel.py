#multilevel inheritance
class Mec:
    def __init__(self,workshop):
        self.workshop=workshop
        print("Mec")
    def display(self):
        print(" I am from Mec")
class Ent:
    def __init__(self,lab):
        self.lab=lab
        print("ENt")
    def display(self):
        print("I am from Ent")

class Mectronix(Mec,Ent):
    def __init__(self,workshop):
        super().__init__(workshop)
m=Mectronix("Yes")
m.display()
c=Ent("yes")
c.display()