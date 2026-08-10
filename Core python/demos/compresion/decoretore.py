#def demo():
    #print("i am in demo")
#x=demo
#(type(x))
#demo
#x()

#def outerfun():
    #print(" i am in outer")
    #def innerfun():
        #print("hello")
    #return innerfun
#a=outerfun()
#print("++++++++++++++")
#a()
#outerfun()

def decoretor(fun):
    print("i am in decoretor")
    def wrapper():
        print("before funcation call")
        fun()
        print("after function call")
    return wrapper
def fun():
    print("i am from function")
x=decoretor(fun)
x()
def fun():
    print("i am from function")
x=decoretor(fun)
x()
