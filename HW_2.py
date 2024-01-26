"""
Write a function to find the maximum of 3 variable. 
a) You will accept the values outside function and then pass it. 
b) You will write the logic inside the function and return the value.
c) You will print the numbers using print and format arranging in ascending order

"""

def big (x,y,z):
    if x > y:
        if x > z:
            return x
    elif y > z:
        return y
    else:
        return z
    

# x = int(input("Choose first number"))
# y = int(input("Choose second number"))
# z = int(input("Choose third number"))
# x = 3
# y = 5
# z = 1
x,y,z = 1,2,4
print (big(x,y,z))