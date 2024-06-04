# a = ["Suits","Vampire","Originals"]
# b = ("Friends","Big Bang")#---> tuple and the adding the values
# a.extend(b)
# print(a)
# print(len(a))#---> length of a 4
# print(a[0])#--->Access of list items 
# print(a[3])
# print(type(a))
# print(type(b))
# a.remove("Big Bang")
# print(a)
'''
list is store multiple items in one variable 
list is mutable, change, order and allow duplicate values
'''


'''
adding two values
extend one variable
find the length
what is the access value of -1
remove the banana
'''
# x.append("Blueberry")
# x.append("mango")
# y=["Green Apple","Ice Apple","Dragon Fruit"]
# x.extend(y)
# print(x[-1])
# print(len(x))
# x.remove("banana")
# x.pop(1)#remove the specified index
#del x #x will be deleted all the values
# x.clear()#method empties the lists
'''
for loop
'''
x =["apple", "banana", "cherry"]
[print(i) for i in x]
# print(x[0])
# print(x[1])
# print(x[2])
# for i in x:
#     print(i)
'''
for loop specified index 
'''
# for i in range(len(x)):
#     print(i)

'''
while loop
'''
# i = 0 # 1,2
# while len(x)>i:# 2 < 3 True
#     print(x[i])# cherry
#     i += 1#i=1+1 ==>2
#     #break #skips the current iteration 
if "chery" in x:
    print("okay")
else:
    print("not okay")

'''
Lists Comprehension
'''
a = ("vivo","sony","samsung","lebara","infinix")
c = list(a)

'''
tuple is an ordered , unchange and allow duplicate values
set is an unordered , unchange and no duplicate values
'''
b = [i for i in a if "n" in i]
# b  = [expression for item in iterable if condition is true ]
# for i in a:
#     if "o" in i:
#         b.append(i)
print(b)

