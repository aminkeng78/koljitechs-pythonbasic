
import builtins

thisdict = {"brand": "ford", "model": "mustang", "year" : 1990}
thisdict["brand"] = "toyota"
#print(thisdict)

### what if the key doesn't exist
thisdict = {"brand": "ford", "model": "mustang", "year" : 1990}
thisdict["country"] = ["Nigeria", "cameroon", "Ghana"]
#print(thisdict)


#operation with dictionary
keys = {'a','e', 'i', 'o', 'u'}

vowels = thisdict.fromkeys(keys)
#print(vowels)

keys = {'a','e', 'i', 'o', 'u'}
value = [1,2]
vowels = thisdict.fromkeys(keys,value )
#print(vowels)

new_dict = {'brand': 'ford', 
            'model': 'mustang', 
            'year': 1990, 
            'country': ['Nigeria', 'cameroon', 'Ghana']}
#print(new_dict.get('country'))

#print(new_dict['country'])

###key() method in dict
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}
king=(people.get(4))
#print(king.get("age"))
#print(f"the age of mr Peter is {king.get('age')}")

# Assignment 
products = [
    ("product_1", 200),
    ("product_2", 400),
    ("product_3", 900),
    ("product_4", 1000)
]
# print out all the prouct that is greater than 500
#for item in products:
    #print(item)
    #if item[1] >= 500:
        #print(item)
#for product in products:
    #if product[1] >= 500:
        #print(product)   
#print(products)
result = filter(lambda product:product[1] >=500, products)
print(list(result))