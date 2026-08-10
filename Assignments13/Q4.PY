#4. Python Program to Generate a Dictionary that Contains Numbers (between 1
#and n) in the Form (x,x*x).
n=int(input("enter a number:"))
d={}
for i in range(1,n+1):
    d[i]=i*i

    #dispaly
    print("dictnary:")
    print(d)
