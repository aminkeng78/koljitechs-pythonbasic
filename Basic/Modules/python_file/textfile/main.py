
import time
# how to work with files
# files===> extensions
# how to to work with text file using python ---->

#how to open a textfile
#open("filename", mode="r" "w" "a" "+")
#open("textexample", 'w')
'''
path = input("enter the file name")
file = open(path, 'r')
data = file.read()
print(data)


file.close()
#print(dir(file))

path = "textexample.text"

with open(path, 'r') as file:
    #data = file.read()
    data = file.readlines()
    print(data)

# write the file with python
path = "textexample.text"
with open(path, 'r') as file:
    #data = file.read()
    data = file.readlines()
    #print(data)
with open("writing_data.txt", 'w') as file:
    #data = file.write("Adulthood na scam")
    #print(data)
    file.writelines(data)
    
with open("writing_data.txt", 'w') as file:
    #data = file.write("Adulthood na scam")
    #print(data)  
    file.write("You gast to hustle, make a living 24/7")
    file.write("Nobody go ask if you don chop\n")
    file.write("Nobody go send you free money\n")
    file.write("If you no get na you sabi") 
     
'''
with open("writing_data.txt", 'a') as file:
    
    file.write("Adulthood na scam\n")
    time.sleep(3)
    file.write("You better get am for your mind\n")
