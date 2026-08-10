#three list of number their square and cube
n=int(input("enter how many number:"))
numbers=[]
square=[]
cube=[]

for i in range(1,n+1):
    numbers.append(i)
    square.append(i**2)
    cube.append(i**3)

    print('number:',numbers)
    print('square:',square)
    print('cube:',cube)
