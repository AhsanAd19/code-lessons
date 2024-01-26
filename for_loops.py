x = "job"
y = "                  Have a nice day                  "
z = """my name is adiyat
my fav color is blue
"""
capital_y = y.upper()
lower_y = capital_y.lower()
print (x[1])
print(y[0:4])
print(y[5:])
print(capital_y)
print(lower_y)
print(y.strip())
print(x.replace("j","J"))
print(x.split())
print(y.split())
print(z.split())

print(z[3:7])

for i in z.split():
    print (i)

split_string = z.split()
print(split_string[-3])