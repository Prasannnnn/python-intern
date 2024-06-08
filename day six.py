#last day class revision
'''
inner class
inheritance
-->single
-->multi
-->multiple
'''
'''
today
--->constructor in inheritance 
--->super
--->MRO
'''
class Hollywood:
    def __init__(self) -> None:
        print("Hollywood")

    def avg_movies(self):
        print("fall guy,bad boys, la la land, barbie, downsizing")

    def scifi(self):
        print("Truman,oppenhimer,big bang theory")

    def comics(self):
        print("Iron man,batman,justice league, dark night")

class Kollywood:
    def __init__(self) -> None:
        print("Kollywood")


    def thalapathy(self):
        print("theri,gilli,kuruvi,goat")

    def thala(self):
        print("Mankatha,Billa")

    def ulaganayagan(self):
        print("Vikram")

    def star(self):
        print("Sivaji")


class Molly(Kollywood,Hollywood):
    def __init__(self) -> None:
        super().__init__()
        print("Mollywood")
    def lalettan(self):
        print("Bro daddy")

    def mamo(self):
        print("Bheeshma")


#a = Molly()


'''
Polymorphism
poly ---> many
morphism ---> forms
it is an many forms
'''

'''
Duck Typing
---> Duck it can walk
---> Duck can quack
---> Duck can Fly
'''
class VScode:
    def excute(self):
        print("Compiling")
        print("Running")

class edit:
    def excute(self):
        print("AI")
        print("clear errors")

class Laptop:
    def code(self,ide):
        ide.excute()

ide = edit()

a = Laptop()
a.code(ide)


'''
Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
say we have three classes: Car, Boat, and Plane, and they all have a method called move():
'''

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()