#6. Python Program to Multiply All the Items in a Dictionary
d={
    'a':1,
    'b':2,
    'c':3,
    'd':9
}
mult=1
for i in d:
    mult=mult*d[i]
print("multiplication of all items:",mult)