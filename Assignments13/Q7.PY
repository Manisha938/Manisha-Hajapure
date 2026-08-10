#7. Python Program to Remove the Given Key from a Dictionary
d={'a':10,'b':20,'c':30}
key=input('enter the key to remove:')
if key in d:
    d.pop(key)
    print(d)
else:
    print('key not fount')