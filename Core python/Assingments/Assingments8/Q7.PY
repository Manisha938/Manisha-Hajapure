#Write a program to find sum of digits of a number.
def sum_of_series(n):
    total=0
    for i in range(1,n+1):
     total=total+i

    return total  
n=int(input('enter the sum of series:')) 
print("sum",sum_of_series(n))
