# class Student:
#     def __init__(self,name,roll) -> None:
#         self.name = name
#         self.roll = roll
#         self.mar = self.Mark()

#     def show(self):
#         print(self.name,self.roll)
#         self.mar.show()
    
#     class Mark:
#         def __init__(self) -> None:
#             self.marks = 96
#             self.cgpa = 9.6
#             self.course = "CSE"
#             self.year = "1st year"

#         def show(self):
#             print(self.cgpa,self.marks,self.course,self.year)



# stu = Student("Naren",789654321)

# stu.show()

'''
Inheritance
Singlelevel 
Multilevel
Multiple Inheritance
'''

class A: # Super class
    def feature(self):
        print("feature is working")

    def major(self):
        print("major is working")
class B: # sub class
    def britania(self):
        print("50/50 is good")

    def parle(self):
        print("Krack Jack")

class C(B,A):
    def lunch(self):
        print("Variety rice")

    def dinner(self):
        print("Noodles")
#a = A()
#b = B()
# a.feature()
# a.major()
# b.britania()
# b.parle()
# b.feature()
# b.major()
#single level inheritance

#Multilevel inheritance
c=C()
c.britania()

#Multiple inheritance
d=C()
d.dinner()
d.britania()