# Passing a value to a function
def ed (a):
    if a>0:
        if a % 2 == 0:
            return ("this number is even")
        else:
            return ("this number is odd")
    else:
        return("Choose a number greater than 0")

y = int(input("Choose a number: "))
print(ed(y))