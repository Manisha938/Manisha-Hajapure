def demo(fun):
    def wrapper(*args):
    
        print("before your main function")
        fun(*args)
        print("after calling the function")
    return wrapper
@demo
def add(a,b):
      print(f"addition={a+b}")

@demo
def sub(a,b):
    print(f"subtraction={a-b}")
@demo
def logIn():
    print("i am in log in")
x=int(input("enter the number1:"))
y=int(input("enter the bumber2:"))
add(x,y)
sub(x,y)
logIn()
