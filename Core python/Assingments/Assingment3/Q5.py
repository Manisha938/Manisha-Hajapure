#
a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
c=int(input('enter the third number:'))

if(a==b and b==c):
    print('Equilateral:')
elif(a==b and a==c or a==b):
    print('isoscels:')
else:
    print('scalene triangle:')