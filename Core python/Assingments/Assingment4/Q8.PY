#WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start=int(input('enter start number:'))
end=int(input('enter end number:'))
i=1
while start <=end:
    if start % 7==0 and start % 5==0:
        print(start)
    start=start+1

