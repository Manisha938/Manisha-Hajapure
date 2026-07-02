#WAP to print all numbers in a range divisible by a given number.
n=int(input('enter the number:'))
num=int(input('enter the divisor:'))

i=1

while i <= n:
    if (i%num==0):
        print(i)
        i=i+1
        

