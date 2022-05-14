###buildins function inpython?

from ast import Num
import builtins
from unicodedata import numeric
# from pprint import pprint

# pprint(dir(builtins))
 
# print("hello world")

# print(len("hello world"))
# [1,2,3,4,5,4]

# print(sum([1,2,3,4,5,4]))

# print(type("hello world"))

#python variables

fist_name = "conilius"
last_name = "aminkeng"
age = 30
print(type(age))
print(type(last_name))
print(type(fist_name))

"my first name is conilius and my last name is aminkeng and my age is 30 years old!"
print(f"my first name is {fist_name} and my last name is {last_name} and my age is {age} years old!")
school = "kojitechs"
class_room = "python"

"my name is conilius, and i school in kojitechs, and i learn python"

print(f"my name is conilius, and i school in {school}, and i learn {class_room}")

#How to name your variables
#aviod using python builtin functions to name your variables

#Built-in Data Types
#Some of the python data types we 
#text =str
type("123456")
#numeric type: int

num = 123456
print(type(num))

#float data type
type(12.3)
#dictionary type:
#mapping
student_info = {"name":"conilius", "age":24}
type(student_info)

#set {}
set_number = {1,2,3,4,5,6,7,8}
type(set_number)
x = {"apple", "banner", "cherry"}
type(x)
#list[]
list_of_items = ["apple", "banner", "cherry"]
print("list_of_items")

#boolean
#Ture,True
#False, false
is_approved = True
is_hot = False
type(is_approved)
print(type(is_hot))
y = None
print(type(y))

