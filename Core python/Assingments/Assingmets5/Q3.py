#no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

#accept the no of passenger
n=int(input('enter the number of passenger:'))

#accept the ticket cost.
ticket_cost=int(input('enter the ticket_cost:'))

total_amount=0
#accept the of each passenger
for i in range(1,n+1):
    age=int(input('enter age of passenger:'+str(i)+" "))
    if age<12:
        amount=ticket_cost-(ticket_cost*30/100)
    elif age>59:
        amount=ticket_cost-(ticket_cost*50/100)
    else:
        amount=ticket_cost
        total_amount=total_amount+amount

        #display
        print("total ticket amount=",total_amount)