#11. WAP to check if given number Strong Number.
n=int(input('enter the strong number:'))
temp=n
sum=0

while temp >0:
    digit=temp % 10
    fact=1
    i=1
    while i <= digit:
        fact=fact*i
        i=i+1
    sum=sum+fact
    temp=temp//10
if sum==n:
    print("strong number:")
else:
    print(" not strong number:")
   

