#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
#5 subject marks
m1=int(input('enter first subject marks:'))
m2=int(input('enter second subject marks:'))
m3=int(input('enter third subject marks:'))
m4=int(input('enter fourth subject marks:'))
m5=int(input('enter fifth subject marks:'))
 #formula
total_marks=m1+m2+m3+m4+m5
percentage=total_marks/5

#disply grade
if percentage>75:
    print('Grede:first class')
elif percentage>90:
    print('Grede:second class')
elif percentage>80:
    print('Grede:third class')
elif percentage>87:
    print('Grede: forth class')
else:
    print('Failed')


    



