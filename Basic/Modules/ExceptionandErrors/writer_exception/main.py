'''
a = 10
b = 0
c = a / b
print(f"{a} / {b} is = {c}")

#to hand this 
try:
    a = 10
    b = 0
    c = a / b
    print(f"{a} / {b} is = {c}")
except:
    print("can't divide with zero please provide df number")
print("i love python")
'''
'''
try:
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    c = a / b
    print(f"{a} / {b} is = {c}")
except ValueError:
    print("enter wrong number")
except ZeroDivisionError:
    print("can't didvid with zero please provide df number")
''' 
''' 
try:
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    c = a / b
    print(f"{a} / {b} is = {c}")
except (ValueError, ZeroDivisionError):
    print("please Enter value valid")

try:
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Enter  valid value")
finally:
    print("inside finally block")
    
 ''' 
'''  
try:
     file = open("file1.sh","r")
     data=file.readline()
     print(data)
except Exception as e:
    print("file not found",e)
finally:
    file.close()
'''
#Raising an Exception
#(1,10)
#To calculate interest rate (amount, year, rate) /100
''' 
def simple_interest(amount, year, rate):
    try:
        if rate >10:
            raise ValueError("rate")
        interest = (amount, year, rate)
        print(interest)
    except ValueError:
        print("intrest rate is not in rage of 10")
        
        
''' 
amount =100
year = 1
rate = 10      
try:
    if rate >10:
     raise ValueError("rate")
    interest = (amount * year * rate)   
    print(interest)
except ValueError:
        print("intrest rate is not in rage of 10")
