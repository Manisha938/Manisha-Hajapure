#Program to Find the Roots of a Quadratic Equation
#take the input
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

#calculate the discriminant
discriminant = b**2 - 4*a*c

#check the nature of the roots
r1=(-b + discriminant**0.5)/(2*a)
r2=(-b - discriminant**0.5)/(2*a)

#result
print(f"The roots of the quadratic equation are: {r1} and {r2}")