
# find the minimum & maximum among four numbers & multiply them.

a = 50
b = 20
c = 30
d = 15
min_value = -1
max_value = -1
print("given values:\t", a,b,c,d)

if ((a<b) and (a<c) and (a<d)):
    min_value = a
elif ((b<c) and (b<a) and (b<d )):
    min_value = b
elif ((c<a) and (c<b) and (c<d)):
    min_value = c
elif ((d<a) and (d<b) and (d<c)):
    min_value = d
print ("min_value:\t", min_value)

if ((a>b) and (a>c) and (a>d)):
    max_value = a
elif ((b>c) and (b>a) and (b>d )):
    max_value = b
elif ((c>a) and (c>b) and (c>d)):
    max_value = c 
elif ((d>a) and (d>b) and (d>c)):
    max_value = d
print ("max_value:\t", max_value)    
var = min_value * max_value

print (min_value ,"*" ,max_value, ":\t", var)






