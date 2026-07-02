#10. WAP to check if given number is Perfect Number.
n=int(input('enter the number:'))
i=1
sum=0

while i<n:
    if i % n==0:
        sum=sum+i
    i=i+1

if sum == n:
    print("perfect number:")
else:
    print("not perfect number:")