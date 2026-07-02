#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_userid="manisha"
correct_password="12345"

attempt=1
while attempt<=3:
    userid=input('enter the userid:')
    password=input('enter the password:')

    if userid==correct_userid and password==correct_password:
        print("login successfully")
        break
    else:
        print("incorrect userid or password")

        attempt+=1
        if attempt>3:
            print("3 attempts complated program terminate.")