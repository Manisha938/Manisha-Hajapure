#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
total_amount=0
 
for i in range(1,6):
    print('\n person',i)
age=int(input('enter your age:'))
ticket_amount=int(input('enter your ticket_amount:'))

if age<12:
    discound_ticket= total_amount*30/100
elif age<55:
    discound_ticket= total_amount*50/100
elif age<90:
    discound_ticket= total_amount*50/100
elif age<21:
    discound_ticket= total_amount*50/100
else:
    dicount=0

#calculate finial amount
final_amount=ticket_amount-discound_ticket
print("finial ticket amound for this person:",final_amount)

#add to total amount
total_amount+=final_amount
print('total_amount:',total_amount)