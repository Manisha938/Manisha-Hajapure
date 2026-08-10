s1={10,20,30,40}
s2={30,40,50,60}
s3={50,60}

#s1.add(70)
#s1.clear()
#s4=s1.copy()
#print(s1.difference(s2))
#s1.difference_update(s2)
#s1.discard(20)               #20 remove
#print(s1.intersection(s2))
#s1.intersection_update(s2)
#print(s1.isdisjoint(s3))
#print(s3.issubset(s2))       #all elements of s3  are available in s2
#print(s2.issuperset(s3))     #  in all elements of s2 are available  s3
#s2.pop()
#s2.remove(30)                 #30 remove
#print(s1.symmetric_difference(s2))   #30,40 common hei
#s1.symmetric_difference_update(s2)
#print(s1.union(s2))
s1.update({70,80,90})
print(s1)