#Write a program to input any alphabet and check whether it is vowel or consonant.
ch=int(input('enter the character:'))

if ch.lower()in('a','e','i','o','u'):
    print("volwels:")
else:
    print("consonant:")