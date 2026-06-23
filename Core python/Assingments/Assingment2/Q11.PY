#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amt=int(input('enter the amound:'))

n200=amt//200
amt%=200

n100=amt//100
amt%=100

n50=amt//50
amt%=50

n20=amt//20
amt%=20

n10=amt//10
amt%=10

n1 = amt

total_notes = n200 + n100 + n50 + n20 + n10

print("Total notes required =", total_notes)