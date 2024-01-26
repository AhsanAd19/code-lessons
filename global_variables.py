# #global variables
# v = "hi"

# def printing_string (v):
#     #local variable
#     v = "hello"
#     print (v)

# printing_string(v)
# print (v)


#global variables
v = "hi"

def printing_string ():
    global v
    v = "hello"
    print (v)

printing_string()
print (v)