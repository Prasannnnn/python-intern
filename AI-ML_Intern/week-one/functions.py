'''
functions
is a block of code
'''
a = "Good Morning"
print("Welcome to the world of tamil")
'''
create a function
'''

def morn():
    print("Good Morning")

'''
function a call
'''
morn()


def add(a,b):
    return a+b

print(add(5,6))

'''
Types of Functions
default Argument
Posistional Argument
keyword Argument
Arbitrary Argument
'''

#default argument
def fun(x,y=50):
    print("x : " ,x)
    print("y : ", y)

fun(10,25)


#posistional Argument
def nameage(name,age):
    print("Hi , My name is ", name)
    print("My age is ,",age)

nameage("Suraj",24)
nameage(24,"Suraj")

#Arbitrary Argument
# *args (non keyword Argument)
# **kargs(Keyword Argument)


def names(*args):
    return args

a = names(1,2,3,4,5,6)
print(a)


def mun(**kargs):
    for keys,values in kargs.items():
        print("%s == %s " % (keys,values))

mun(first = 'Running',second = 'up',third = 'that',fourth ='hill', fifth ='kate',six = 'selena')