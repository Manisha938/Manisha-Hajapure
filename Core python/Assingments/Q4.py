#Write a program to enter P, T, R and calculate simple Interest.
#take the input
P=int(input('enter the principal amount:'))
R=int(input('enter the rate of interest:'))
T=int(input('enter the time period:'))

#put the formula
SI=(P*R*T)/100

#result
print(f'simple interest= {SI}')
