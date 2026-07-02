for i in range(1, 6):       #row number
  
  for j in range(1, 6 - i): #space print
      print(' ',end= ' ')

  for j in range(1,  2 * i): #star print 2*1 odd
      print('*', end=' ')
  print()

for i in range(4, 0, -1):    #lower half
   for j in range(1 , 6 - i): #space increase
         print(" " , end=" ")

   for j in range(1 , 2 * i): #star decrese
        print("*", end=" ")    
   print()
  