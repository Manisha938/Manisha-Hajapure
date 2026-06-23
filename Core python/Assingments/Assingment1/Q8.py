#Write a program to convert days into years, weeks and days.
#take the input
days = int(input("Enter the number of days: "))

#perform the operations
years = days // 365
days= days % 365

weeks = days // 7
days = days % 7

#result
print(f"{years} years, {weeks} weeks, and {days} days")
