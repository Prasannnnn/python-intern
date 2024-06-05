# a = {
#     "name":"hema",
#     "age":24,
#     "Role":'studying',
#     "College":'CMC College'
#     }
# # print(a)---> Dictionary callable
# #access of dictionaries
# # b = a["name"]
# # c = a["age"]
# #using get
# b=a.get('College')
# print(b)

# #keys return a list of all the keys in a dictionary

# c = a.keys()
# print(c)

# a["area"]="Arani"
# print(a)

# '''
# Get values

# ---> c = a.values()
# generally print the values of the dictionary
# '''
# d=a.values()
# print(d)

# '''
# Get items
# return each item in dictionary
# '''

# # e = a.items()
# # print("items",e)

# # a["area"]="vellore"

# # print(a)

# '''
# update dictionary
# '''
# a.update({'area':'Vadalur'})

# print(a)


# '''
# Loop dictionaries
# '''
# for x in a:
#     print(x)

# fri = {
#     "a" : {
#         "name":"Pradeep",
#         "age":22
#     },
#     "b" :{
#         "name":"Pranash",
#         "age":23
#     }
# }
# print(fri["a"]["age"])



'''
odd ---> weird
even range (6,20) ---> not weird
even greater (20)---> not weird
'''

# def add(a,b):
#     return a+b
# print(add(10,5))

'''
user two inputs a and b
Arithmetic Operations +,-,*,/,//,%,**
a = 10
b = 5
operators = add
15
Use Functions
'''


def arithmetic_operations(a,b,operator):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b
    elif operator=="%":
        return a%b
    elif operator=="//":
        return a//b
    elif operator=="**":
        return a**b   
a=int(input("Enter a number:"))
b=int(input("enter number2:"))
operator=input("Enter any arithmetic operators:")
c=arithmetic_operations(a,b,operator)
print(c)
'''
Functions
'''


'''
Recursions
'''
def power(a,b):
    if b!=0:
        return a*power(a,b-1)
    else:
        return 1
a=float(input())
b=float(input())
print(a,"to the power",b,"is", power(a,b))


