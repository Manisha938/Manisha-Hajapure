#prime number or not using recursive
def prime(n,i):
    if i==1:
        return True
    if n % i ==0:
        return False
    return prime(n,i-1)

num=int(input('enter the number:'))
if num <= 1:
    print(False)
else:
    print(prime(num,n-1))