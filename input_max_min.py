# Write a program to find the largest of three numbers (example: a = 10, b = 30, c= 20, largest is b)
a = (int(input("enter the number1:\t")))
b = (int(input("enter the number2:\t")))
c = (int(input("enter the number3:\t")))

if (a>b and a>c):
    print("a is maximum:\t", a)
elif (b>a  and b>c):
    print ("b is maximum:\t", b)
elif (c>a and c>b):
    print ("c is maximum:\t", c)

if (a<b and a<c):
    print ("a is minimum:\t", a)
elif (b<a and  b<c):
    print ("b is minimum:\t", b)
elif (c<a and c<b):
    print ("c is minimum:\t", c)