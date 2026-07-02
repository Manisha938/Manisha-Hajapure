#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#e. x - x2/3 + x3/5 - x4/7 + .... to n terms

#a
#n=int(input('enter n number:'))
#sum=0
#fact=1
#for i in range(1,n+1):
    #fact=fact*i
    #sum=sum+fact
    #print('sum=',sum)
#b
#n=int(input('enter n:'))
#sum=0
#for i in range(1,n+1):
    #sum=sum+n**i
    #print("sum",sum)
#c
n=int(input('enter number:'))
sum=0
temp=1
for i in range(1,n+1):
    sum=sum+temp
    temp=temp**2
    print("sum=",sum)

#d
a=int(input('enter a number:'))
sum=0
for i in range(1,11):
    sum=sum+(a**i)
    print("sum=",sum)

#e
x=int(input('enter x number:'))
n=int(input('enter number of term:'))
sum=0
sign=1
a=1

for i in range(1,n+1):
    sum=sum+sign(x**i)/d
    sign=sign*-1
    d=d+2

    print("sum=",sum)
