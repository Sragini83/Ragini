# largest of three numbers (example: a = 10, b = 30, c= 20, largest is b)
    
a = 50
b = 90
c = 70
largest= -1
var_name = "unknown"

if ((b>a) and (b>c)):
    largest = b
    var_name = "b"
elif ((a>b) and (a>c)):
    largest = a
    var_name = "a"
else:
    largest = c
    var_name = "a"

print("largest variable name : ", var_name, "largest value: ", largest)

