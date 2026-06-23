#Write a program to swap two numbers using third variable.
#take input from the user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print(f"Before swapping: x = {x}, y = {y}")

#swap using a third variable
z=x
x=y
y=z
print(f"After swapping: x = {x}, y = {y}")
