#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
n=int(input("enter thr student number:"))
total_percentage=0
for i in range(1,n+1):
    print("student:",i)
    total=0
    for j in range(1,6):
        marks=int(input('enter the marks of students{j}:'))
        total+=marks
        percentage=total/5
        print("percentage=",percentage,'%')

        total_percentage+=percentage

        average=total_percentage/n
        print("average percentage of student=",average,'%')


