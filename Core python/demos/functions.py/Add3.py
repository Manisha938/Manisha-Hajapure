#without passing parameter with return value
def Addition():
    num1=int(input('enter a number1:'))
    num2=int(input('enter a number2:'))
    
    sum=num1+num2

    return sum
res=Addition()
print(f"Addition is ",res)

   