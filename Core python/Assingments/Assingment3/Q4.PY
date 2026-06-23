##Write a program to input angles of all sides of triangle and check whether triangle is valid or not.
#take the inputs values

a=int(input('enter the first side:'))
b=int(input('enter the second side:'))
c=int(input('enter the third side:'))

if(a+b>c)and(a+c>b)and(b+c+a):
    print('all sides of triangle  valid:')
else:
    print('all sides of triangle  not valid:')