#Find the sum of three-digit number.
#take input from the user
num= int(input("Enter a three-digit number: "))

#check if the number is three-digit
d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

sum_of_digits = d1 + d2 + d3
print(f"The sum of the digits of the number is: {sum_of_digits}")