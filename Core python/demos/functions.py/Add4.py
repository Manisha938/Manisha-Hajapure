#with passing parameter with return value
def Addition(num1,num2):
    sum=num1+num2
    return sum

x=int(input('enter a number:'))
y=int(input('enter a number:'))

res=Addition(x,y)
print("Addition",res)

