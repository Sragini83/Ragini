
#Write a program to find out the min and max among four numbers and multiply them, 
#example: a = 10, b = 20, c = 30, d = 15  minimum = 10, 
#maximum = 30, output must look like this: 10*30 = 300

a = (int(input("Enter the number1:\t")))
b = (int(input("enter the number2:\t")))
c = (int(input("enter the number3:\t")))
d = (int(input("enter the number4:\t")))
print ("********************************")
print ("number1:",  a, 
    "\nnumber2:",  b,
    "\nnumber3:", c,
    "\nnumber4:", d)

min_vaue = 99999 
max_value = -1

if (a<b and a<c):
    min_value = a
elif (b<a and b<c):
    min_value = b
elif (c<a and c<b):
    min_value = c
print ("minimum value :\t", min_value)

if (a>b and a>c):
    max_value = a
elif (b>a and b>c):
    max_value = b
elif (c>a and c>b):
    max_value = c
print ("maximum value:\t", max_value)

var = min_value * max_value
print ("multiplication :\t", var)