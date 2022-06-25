####Identity OPERATION
import getpass
y = 3
x = 2
y == x
print(y==x)
name = "koji"
second_name = "Bello"
print(name == second_name)

passwd = "king123"
#user_passwd = input("what is your password")
user_passwd = getpass.getpass("what is your password")
if user_passwd == passwd:
    print("login successful")
else:
    print("login unsuccessful")
    
