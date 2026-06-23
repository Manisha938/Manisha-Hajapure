no=int(input("enter the number:"))
if no<=1:
    pass
    #print("no is not prime and no comosite mai aalag huu")
else:
    for i in range(2,no):
        if no%i==0:
          print(f"{no}is not prime")
          break
    else:
          print(f"{no}is prime")
    
   

      

