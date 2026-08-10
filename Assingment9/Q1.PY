#strong number using a recursive function
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def sum_fact(n):
    if n==1:
        return 1
    return fact(n)+sum_fact(n-1)

n=int(input('enter the number:'))
res=sum_fact(n)
print(res)
