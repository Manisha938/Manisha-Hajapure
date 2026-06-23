#12. Write a program to check if given 3 digit number is a palindrome or not.
num=int(input('enter the 3 digits number: '))
temp=num

rev=(num%10)*100+((num//10)%10)*10+(num//100)

if temp==rev:
    print("palidrom number:")
else:
    print("not a palidrom number:")