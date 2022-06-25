
#Codition in Python
#import pprint
from pprint import pprint
'''
 if => True:
     Do something:
else:
   Do nothing
'''
''''
x = 4
y = 2
if (x > y):
    print(f"{x} is greater than {y}")
    
    ## what if we don't know the value of x or y?
    x = eval(input("Enter number:"))
    Y = eval(input("Enter number:"))
    if (x > Y):
        print(f"{x} is greater than {Y}")
    else:
        print(f"{x} is greater than {Y}")
  '''      
#print(list(range(1 ,20)))
''''
###for loop with if
numbers = list(range(1 ,11))
for number in numbers:
    if number==1:
        print("one")
    elif number==2:
        print("two")
    elif number==3:
        print("three")
    elif number==4:
        print("four")
    elif number==5:
        print("five")
    elif number==6:
        print("six")
    elif number==7:
        print("seven")
    elif number==8:
        print("eight")
    elif number==9:
        print("nine")
    elif number==10:
        print("ten")
    else:
        print(f"{number} is out of range, please select between 1-10")
        
user_input = eval(input("Enter number:"))
if user_input==1:
    print("One")
elif number==2:
    print("two")
elif number==3:
    print("three")
elif number==4:
    print("four")
elif number==5:
    print("five")
elif number==6:
    print("six")
elif number==7:
    print("seven")
elif number==8:
    print("eight")
elif number==9:
    print("nine")
elif number==10:
    print("ten")  
else:
    print(f"{user_input} is out of range 1-10") 
'''
''''
user_input = eval(input("  plese enter number:"))

#for user in range(1, 100):

if user_input % 3 == 0 and user_input % 5 == 0:
    print ('FizzBuzz', user_input)
elif user_input % 3 == 0:
    print ('Fizz', user_input)
elif user_input % 5 == 0:
    print ('Buzz', user_input)
else:
    print(user_input)
    '''
hello = "my name is Koji Bello and i love python and i teach python"
# hello= hello.split()
# hello_couts = collection.counter(wor)

# for hello,count in sorted(hello_couts.items()):
#     prin(% )
#print(each_char)
all_freq = {}
for each_char in hello:
    if each_char in all_freq:
        all_freq[each_char] += 1
    else:
        all_freq[each_char] = 1
#res = max(all_freq,key = all_freq.get(each_char))
pprint(all_freq)
     
     
    
