#Write a program to print all numbers which are divisible by m and n in the list.
start=int(input("enter strat:"))
end=int(input('enter end:'))

m=int(input("enter m:"))
n=int(input("enter n:"))

i=start
while i<= end:
    if i % m==0 and i % n==0:
        print(i)
    i+=1