import builtins
## TYPES OF OPERATORS
  #Arithmetic Operation
   
#x = eval(input('enter first number'))
#y = eval(input('enter second number'))
#c = x + y
#print(f"the result of {x} and {y}: {c}")
# xx = 4**4
# print(xx)  

# xx = 100-50
# #print(xx)
# xx = range(1001)
# #print(xx)
# hund = list(range(1,100))
# for i in hund:
#     if i%2==0:
        #print(f"even:{i}")
    #else:
        #print(f"odds:{i}")

###COMPARISON OPERATION
## Takes Values as input, performs some operation print True or False
'''
king = 2==4
print(king)

king = 2>=4
print(king)

king =100>=100
print(king)
temperation = 15
if temperation > 30:
    print("it's hot outside.\nplease drink water!")
else:
    print("it's cold\nGet a jacket")
policy applicant must be obove 18 years
the applicant must not be a student!
print("Congrants Mr Koji\nLoan Granted")


Ooooopsss
print("Sorry you were not approve😔")
'''

age_of_the_applicant = eval(input('provide the age:'))
occupation = input("provide occpation:")
if(age_of_the_applicant > 18 and occupation == "prof"):
    print("good to go")
else:
  print("Sorry you were not approve😔")
    
