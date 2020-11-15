"""
print('Hello World ,This is first Python Program')
print('*'*10)
"""

#variables
"""    
price=10
name="john"
rate=4.9
is_published=True
print(price)

a=10
b=10
c=a+b
print(c)
"""

#Taking Input from the User
""" 
name=input("What is Your Name ? ")
print("Hi "+name)
"""
"""
name=input("What is Your Name ?")
fav_color=input('What is your Fav color ? ')
print("My name is " +name+"and my favourite color is "+fav_color)
"""


#Type Conversion
"""
birth_year=input("BirthYear ?")
age=2020-int(birth_year)
print(age)
print(type(age))
"""
""" 
weight_lbs=input('Weight(lbs): ')
weight_kg=input(weight_lbs)*0.45
print(weight_kg)
"""

#Strings

""" 
course="Python For Beginers"
#print(course)
#print(course[0])
#print(course[-1])
#print(course[0:3]) #first 3 charecter will be print
#print(course[1:0]) #first char will be remove
#print(course[:5])
print(course[1:-1])#first char and last char will be remove
"""

#Formated Strings
""" 
first_name='John'
last_name='Doe'
full_name= 'His name is '+first_name+'and '+last_name
print(full_name)
"""
""" 
first_name='John'
last_name='Doe'
message=f'{first_name}{last_name}is a programmer'
print(message)
"""

#String Methods
""" 
s="Hello World"
print(len(s))
print(s.upper())
print(s.lower())
print(s.replace('Hello','GoodBye')) #replacement will be print
print('Hello ' in s) #Finding Hello 
print(s.find('W')) #Finding W
"""

#Arithmatic Operators
"""
print(10+3)
print(10/3)
print(10//3) #integer number will be print
print(10**3) #exponent number will be print

"""

"""
x=10
x=x+10
print(x)
"""

#Operator Precedence
""" 
x=10+3*3
print(x)
"""
"""
x=10+3*2**2
print(x)
"""

#Math Functions
""" 
x=2.9
print(round(x))

y=2.9
print(abs(-2.9))

import math
#print(math.ceil(8.9))
print(math.floor(5.6))
"""

#if-else statements
""" 
age=18
if age>=18:
    print('Voter')

else:
    print('Not Voter')
"""
""" 
has_income=True
has_credit=True
if has_income and has_credit :
    print('Eligible For Loan')

else:
    print('Not Eligible For Loan')
"""
#while-loop
""" 
i=1
while i<=5
    print(i)
    i=i+1
"""
#for-loop
"""
for item in 'Python':
    print(item)
"""
""" 
for item in ['Mosh','John','Sarah']:
    print(item)
"""
""" 
for x in range(4):
    print(x)
"""

#Nested For Loop
""" 
for x in range(4):
for y in range(3):
    print(f'({x},{y})')
"""

#LIST
""" 
names=['john','bob','mosh']
print(names)
print(names[0])
print(names[0:1])
"""
#2d List
""" 
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
"""

#List Methods
""" 
numbers=[5,35,1,7,4]
#numbers.index(0,10)
#numbers.append(20)
#numbers.remove(5)
#numbers.clear()
#numbers.pop()
#numbers.index(5)
#print(50 in numbers)
#print(numbers.count(5))
numbers.sort()
print(numbers)
"""

#Tuples
#Tuples are similar to list ,so we can use them to store a list of items.But unlike lists we can not remove existing items.Tuples are immutable .we can not mutate or change them.Tuple object doesnot support item assignment

#Unpacking
"""
coordinate=(1,2,3)
x,y,z=coordinate
print(x)
print(y)
print(z)
"""

#Dictionaries
""" 
customer={
    "name":"John Doe",
    "age":30,
    "is_verify":True

}
customer["name"]="Jack"
print(customer["name"])
"""

#Function
"""
def great_user():
    print("Hello Function")

great_user()

def sum(num1,num2):
    return num1+num2
total=sum(10,20)
print(total)
"""

#Exceptions
"""
try:
    age=int(input('Age:'))
    print(age)

except Value_Error:
    print('Invalid Value')
"""
""" 
try:
    age=int(input('Age:'))
    income=2000
    risk=income/age
    print(age)

except ZeroDivisionError:
    print('Age cannot be count 0')
except Value_Error:
    print('Invalid Value')
"""
