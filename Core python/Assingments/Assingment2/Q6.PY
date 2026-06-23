#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
#take input from user
basic=float(input('enter basic salary of employee:'))

#calculate allowances
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

#calculate total salary
total_salary = basic + da + ta + hra

#result
print(f"The total salary of the employee is: {total_salary}")