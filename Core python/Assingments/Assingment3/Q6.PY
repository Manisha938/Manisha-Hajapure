#Write a program to calculate profit or loss.c
cp=int(input('enter the cost price:'))
sp=int(input('enter the selling price:'))

if (sp>cp):
    profit=sp-cp
    print('profit=',profit)
elif (cp>sp):
    loss=cp-sp
    print('loss=',loss)
else:
    print('no profit no loss:')