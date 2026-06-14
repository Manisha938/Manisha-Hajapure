#10. Write a program to calculate area of an equilateral triangle.
#take the input
side_length = float(input("Enter the length of the side of the equilateral triangle: "))

#calculate the area
area = (3**0.5)/4 * side_length**2

#result
print(f"The area of the equilateral triangle is: {area}")