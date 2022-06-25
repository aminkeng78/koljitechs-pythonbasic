## Docstring
'''

def sending_notification(name):
    """this functiopn isto send message to default user
    parameter1(int):user name
    Argument: one argument
    Return:
    None
    """
    print(f"hello { name} you payment is due!")


sending_notification("conilius")
'''
'''
#def listAllinstances(num):
def listAllinstances(*args):
    print(f"here are all the instances {args}")


listAllinstances("instances1", "instances2", "instances3")
'''

'''
def population(name,*args):
    print(f"this is the house of {name}\nWe have {args}")
    
def address(address, city):
    print(f"the address is {address}\nthis city is {city}")

#def main(): 
def user_info(**kwargs):
    print(type(**kwargs))
    print(kwargs)
user_info(name="conilius", age=24, subjec="python")
'''
'''
#for i in range(1, 100):
def fizzbuzz(n):
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
        
        
fizzbuzz(7)         
''' 
'''      
def retun_fizzbuzz(n):
    if n % 15 == 0:
        return("fizzbuzz")
    elif n % 3 == 0:
        return("fizz")
    elif n % 5 == 0:
        return("buzz")
    else:
        return(n)
    return(none)
        
        
response =retun_fizzbuzz(9)
print(response)
'''

def retun_fizzbuzz(n):
    if n % 15 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return(n)
    return(none)
        
user_input = eval(input("enter number:"))      
response =retun_fizzbuzz(user_input)
print(response)