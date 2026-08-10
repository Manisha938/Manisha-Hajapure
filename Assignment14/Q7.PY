#7. Given two sets of numbers, write a Python program to find the missing
#numbers in the second set as compared to the first and vice versa.
#Use the Python set.
#frist set
set1={1,2,3,4,5,6,7,9}

#second set
set2={4,5,6,7,8,9,10,9,1,}

print("missing in second set")
print(set1-set2)

print("missing in frist set:")
print(set2-set1)