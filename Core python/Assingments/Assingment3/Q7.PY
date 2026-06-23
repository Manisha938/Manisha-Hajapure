#Write a program to check if user has entered correct userid and password.
userid="admin"
password=1237

#take the value user
userid=input('enter the userid:')
password=int(input('enter the password:'))

if userid=="admin"and password=="1237":
    print('both are correct:')
else:
    print('both are not correct:')