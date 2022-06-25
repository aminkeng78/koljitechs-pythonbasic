## for l00
from itertools import count
from pprint import pprint
'''
list_1 = ["apple", "orange", "pawpaw", "pear", "cherry"]
for each_item in list_1:
    #print(each_item)
    item = [item for item in list_1]
    print(item)
list_2 = "apple"
for each_item in list_2:
    print(each_item)
'''  
'''
items = ["apple", "orange", "pawpaw", "pear", "cherry"]
for item in items:
    print(item)   
    #if item == "apple":
    if item == "pear":
        break 
'''
'''
numbers = range(1 ,10)
for number in numbers:
    print(number)
    if number == 6:
       # print(number)
        break
    
items = ["apple", "orange", "pawpaw", "pear", "cherry"] 
for item in items:
    print(item)
    if item == "pawpaw":
        continue
'''
'''
fruits = ["apple", "pawpaw", "orange", "pear", "mango"]
user_data = x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [ {"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1} ]
}

magic_number = [(1,2),(23,4),(23,8)]
hello = "My name if koji Bello and i'm the lead Devops Engineer at plastig"
#[item for item in items]
for fruit in fruits:
    print(fruit)
# for user in user_data:
#     print(user)
for user in user_data.items():
    print(user)
'''
   
name = "marilya mennen", ""
     
count = 0
for m in name:
    if m != "m":
        continue
    else:
        count = count + 1
print("the amount of time m occurred is", count)