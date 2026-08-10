#6. Write a Python program to find the two numbers whose product is
#maximum among all the pairs in a given list of numbers. Use the
#Python set.
#list of number
frist=[2,5,6,7,8,3]

#remove duplication
s=set(frist)
#convert
num=list(s)

max_product=0
a=b=0

#find max 
for i in range(len(num)):
    for j in range(i+1,len(num)):
        product=num[i]*num[j]
        if product >max_product:
            max_product=product
            a=num[i]
            b=num[j]
    print("numbers:",a,b)
    print("maximum product:",max_product)