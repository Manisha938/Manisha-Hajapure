#factorial using the recursive
def Factorialofnum(n):
    if n == 0:
        return 1

    else:
        return n * Factorialofnum (n-1)

n=int(input('enter a number:'))
res=Factorialofnum(n)
print("factorial",res)