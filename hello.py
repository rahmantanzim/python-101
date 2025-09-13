print("Hello World")

# Indentation 
if 5 > 2:
    print("five is bigger than two")

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

if 5>3:
    print('5 is bigger')
    print('3 is smaller')

# In Python, variables are created when you assign a value to it:

course = 9818 
department = 'Software ENG'
print(course)
print(department)


""" this is a comment
written in
more than 1 line """

# In python, if you wanna create a global variable inside a fuinction, you can use the 'global' keyword:

x = 'Awesome'

def myFunc():
    global x
    x = 'Sexy'

print("Python is " + x)

myFunc()

print("Python is " + x)


x = 5
y = "John"
print(5 , y) 

x = "Five"

x = str(5)
print(x)
print(type(x))
X = 5
print(x, type(X))
# String can be created either by single or double quote


#variabel name can start with underscore or letter not a number
# Varibale name 

x,y,z = 'Mango','Banana','Cherry'
print(z)

a =  "Student"
print("All of them are "+ a)
#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

x = str(30)
y = "Thirty"
print("Thirtys " + x  )

# for printing something with the plus operator, both side of + has to be in same type

# Global varibales
# variables that are created outside a function are called global variable

#creating a global variable inside a function
def myFunc():
    global aVariable
    aVariable = "Some random string"
myFunc()

print(aVariable)

# also use the global keyword if you wanna change the global variable inside a function

f = "Fantastic"

def funcFantastic():
    global f
    f = "Fun"

funcFantastic()
print(f)
