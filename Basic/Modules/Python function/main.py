

##Python Function
##type of Function (prit and return)
#python has a DRY principle
  ## syntax of creating a function
from ast import arguments

'''
# def function_name(parameter1, parameter2)
#  #function body
#  #writer some action
# function_name(value(argument))
def king123():
    print("python")
    print("blood of Jesus")
    
king123()    
'''

'''
def say_hello(name, age):
    print(f"hello {name} welcome to kojitechs")
    print(f"I'm {age} years old!")
    #SAY HELLO = IS THE NAME OF THE FUNCTION
    #NAME = THAT IS A PARAMETER IS SAY HELLO FUNCTION
    #AGE = THAT IS A PARAMETER IN  SAY HELLO FUNCTION
    
say_hello("koji", 123)


##WRITE FUNCTION TO ADD NUMBER
def add(a, b):
    result = a + b
    print(f" the result of a and b is : {result}")
add ("hello", "world")
'''
'''
def even_numbers(n):
    for i in range(1,n):
        if i % 2 == 0:
            print(i, "is an even number")
        else:
            print(i, "is not an odd number")

even_numbers(30)
'''

# TYPES OF FUNCTIONS
#WE HAVE A PRINT FUNCTION
# A RETURN FUNCTION
'''
def send_email(name):
    print(f"hello { name} you payment is due")
    return None
    
send_email("conilius")
'''
#RETURN SEND EMAIL
def notify(name):
    return(f"hello { name} you payment is due")
    
#print(notify("conilius"))
message = notify("conilius")
with open("message.sh","w") as file:
    file.write(message)
