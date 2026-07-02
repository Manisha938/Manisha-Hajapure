#Write a program to print first n prime numbers.n
n=int(input('enter n:'))
count=0
num=2

while count<n:
    f=0
    for i in range(2,num):
        if num % i ==0:
            f=1
            break
    if f==0:
            print(num)
            count+=1
            num+=1