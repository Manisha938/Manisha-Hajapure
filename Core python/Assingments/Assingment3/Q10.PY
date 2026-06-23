#Write a program to check if person is eligible to marry or not (male age >=21 andfemale age>=18)
Gender=input('enter a gender:(female/male)')
age=int(input('Enter age:'))

if(Gender=='female'):
    if(age>=18):
        print('Girl is eligible for marriage:')
    else:
        print('Girl is not eligible for marriage:')
elif(Gender=='male'):
    if(age>=21):
        print('Boy is eligible for marriage:')
    else:
        print('boy is not eligible for marriage:')
else:
    print('invalid gender:')
