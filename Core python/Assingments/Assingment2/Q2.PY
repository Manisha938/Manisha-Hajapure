#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
#take input from the user
celsius = float(input("Enter temperature in Celsius: "))

#formula
fahrenheit = (celsius * 9/5) + 32

#result
print(f"{celsius}°C is equal to {fahrenheit}°F")