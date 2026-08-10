#4. Write a Python program that finds all pairs of elements in a list whose
#sum is equal to a given value.
frist=[1,2,3,4,5,6,7]
#given value
s=int(input('enter the sum:'))
#find pair
for i in range(len(frist)):
    for j in range(i+1,len(frist)):
        if frist[i]+ frist [j]==s:
               print(frist[i], "+", frist[j], "=", s)
        