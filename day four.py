'''
Recursions
'''
# def pow(a,b):
#     if b!=0:
#         return a*pow(a,b-1)
#     else:
#         return 1

# print(pow(8,2))

'''
add two numbers
'''
# def add(a,b):
#     if b == 0:
#         return a #14
#     else:
#         return add(a+1 , b-1)# (9,5) ---> (10,4) --->(11,3)--->(12,2)--->(13,1)--->(14,0)

# a= int(input("a"))
# b = int(input("b"))
# print(add(a,b))

'''
factorial 6
'''
# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)
    
# x = fact(6)
# print(x)

'''
OOPs Concepts---> Object Oriented Programming
class and objects 
class is nothing but a blueprint 
object is a 

----> class phone apple 15 (blueprint)
----> 100 phones production -----> objects
'''

class Phone: # human
    def config(self):
        print("IOS","16GB Ram","256GB Storage")

i15 = Phone()
i14 = Phone()
i13 = Phone()
i12 = Phone()

Phone.config(i15)
Phone.config(i14)
Phone.config(i13)
Phone.config(i12)

def add(a,b):
    return a

class Human():
    def __init__(self,name,age,blood) -> None:
        self.name = name
        self.age = age
        self.blood = blood

    def __str__(self) -> str:
        return f"My name is {self.name} and the Age is {self.age} and my blood group is {self.blood}"

    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    

person1 = Human("Hema",24,"B+")
person2 = Human("Bhuvi",18,"B+")
person3 = Human("Praveen",22,"O+")
person4 = Human("Pranash",22,"A-")

print(person1)
print(person2)
print(person3)
print(person4)

'''
Inheritance   ---> Single, Multiple, Multilevel and Hybrid
Abstraction   ---> just pass the arguments
Polymorphism  ---> Method Overloading, Operator Overloading
Encapsulation ---> Data Hiding
'''
