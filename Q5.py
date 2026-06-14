#Write a program to enter P, T, R and calculate Compound Interest.
#take the input
P=int(input('enter the principal amount:'))
R=int(input('enter the rate of interest:'))
T=int(input('enter the time period:'))

#put the formula
CI=P*(1+R/100)**T

#result
print(f'compound interest= {CI}')