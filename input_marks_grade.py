#Write a program that will assign grades to the student according to the below scheme
#If (marks>=90) grade A
#If (marks < 90 and marks >= 80) grade B
#If (marks < 80 and marks >= 70) grade C
#If (marks < 70 and marks >= 60) grade D
#If (marks<60) grade E

a = (int(input("enter the sub_marks:\t" )))

if (a>=90):
    print ("grade A")
elif (a<80 and a>=70):
    print ("grade B")
elif (a<80 and a>=70):
    print ("grade C ")
elif (a<70 and a>=60):
    print ("grade D")
elif (a<60):
    print ("grade E")