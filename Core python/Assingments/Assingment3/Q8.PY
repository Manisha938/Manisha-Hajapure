#Write a program to prompt user to enter userid and password. After verifyiuserid and password display a
#  4 digit random number and ask user to enter the same number.
#If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
#correct use id and passwrd
correct_userid="admin"
correct_password="1234"

#user throgh enter
userid=input('enter userid:')
password=int(input('enter password:'))

#verify the password and userid
if correct_userid==userid and password==correct_password:
    print('login successfully:')

#random number
rand_num=random.randint(1000,9999)
print('enter this number',rand_num)

#ask the enter number same or not
user_num=int(input('enter the number same:'))
if user_num==rand_num:
    print('successfull complated:')
else:
    print('failed:')

