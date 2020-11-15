#classes
"""
class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

print1=Point()
print1.move()
print1.x=10
print(print1.x)
"""

#Constructor

""" 
class Point:
    def __init__(self,x,y):
        self.x= x
        self.y= y
point=Point(10,20)
point.x=11
print(point.x)
"""
""" 
class Person:
    def __init__(self,name):
        self.name= name

    def talk(self):
        #print("talk")
        print(f"His name is {self.name}")
        
        john=person("John")
        print(john.name)
        john.talk
"""

#Inheritence
"""
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")


dog1=Dog()
dog1.walk()

"""