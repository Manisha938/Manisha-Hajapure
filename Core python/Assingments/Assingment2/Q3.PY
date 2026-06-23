#Convert distant given in feet and inches into meter and centimeter.
#take input from the user
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

#convert to meters and centimeters
total_inches = feet * 12 + inches
meters = total_inches * 0.0254
centimeters = meters * 100

#result
print(f"{feet} feet and {inches} inches is equal to {meters:.2f} meters or {centimeters:.2f} centimeters.")