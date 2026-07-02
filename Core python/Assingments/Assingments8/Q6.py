#Write a program to find print the following Fibonacci series usingfunctions:
#1 1 2 3 5 8 n term
def fibonacci_series(n):
    a=0
    b=1
    #print(a)
    #print(b)
    for i in range(1,n):
        c=a+b
        print(c)
        a=b
        b=c

n=int(input("enter the fibonacci series:"))

fibonacci_series(n)