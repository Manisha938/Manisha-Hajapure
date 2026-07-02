#Write a program to check if entered year is a leap year or not.
def leap_year(year):
    if(year% 400==0)or(year % 4==0 and year % 100!=0):
    
        print("leap year:")
    else:
        print("not leap year:")

year=int(input('enter number:'))
leap_year(year)