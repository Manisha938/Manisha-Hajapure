def  decoretor(fun):
    def inner():
        print("before calling functanality is added:")
        fun()
        print("after caling functionlity is added")
    return inner
@decoretor           #function calling syntax
def add():
    a=10
    b=20
    print(f"addition ={a+b}")

@decoretor
def sub():
    a=10
    b=20
    print(f"subtraction={a-b}")
add()
print("+++++++++++++++++++++++++++++++++++++++")
sub()