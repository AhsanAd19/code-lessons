x = 4
y = 'hello'
a = 4.556
d = 22/7
print(type(x))
print (type(y))
print (type(a))
print (int(d))

complex = 4j
print (type(complex))

print(float(x))
s = "What's your name"
# Snake case
first_name = "Adiyat"
# Camel Case
lastName = "Ahsan"
age = 14
print (first_name, lastName)
print ("My name is: ", first_name, lastName)
print ("My age is: " + str(age))
print ("My first name is: " + first_name + "My last name is:" + lastName + " My age is " + str(age))
print ("My first name is:{1} My last name is {0} my age is {2}" .format(first_name,lastName,age))
print ("My first name is:{first_name} My last name is {lastName} my age is {age}" .format(first_name = "adiy",lastName = "ah",age = 5))