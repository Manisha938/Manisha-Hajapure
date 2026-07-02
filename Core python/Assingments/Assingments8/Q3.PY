#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!


#def sum_of_series(n):
   # total=0
    #for i in range(1,n+1):
        #total=total+i
    #return total

#n=int(input("enter n:"))
#print(f'sum=',sum_of_series(n))

#b. 1!+ 2! + 3! + 4!+..... + n!
#def factorial(n):
    #fact=1
    #for i in range(1,n+1):
        #fact=fact*i
    #return fact
#n=int(input('enter n factorial:'))
#print(f"factorial of",factorial(n))

#1^1 + 2^2 + 3^3+ ...... n^n
def power_sum(n):
    total=0
    for i in range(1,n+1):
        total=total+(i**i)
    return total

n=int(input("enter n:"))
print(f'sum=',power_sum(n))




