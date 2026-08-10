#Write a Python program to remove the intersection of a second set with a first set.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

B.difference_update(A)

print("First Set:", A)
print("Second Set after removing common elements:", B)