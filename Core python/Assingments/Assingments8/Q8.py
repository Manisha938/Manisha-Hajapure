#Write a program find reverse of a number
def reverse_number(n):
    rev=0
    while n > 0:
       digit=n%10
       rev=rev*10+digit
       n=n//10
    return rev

n=int(input('enter the reverse number:'))
print("number of reverse=",reverse_number(n))


