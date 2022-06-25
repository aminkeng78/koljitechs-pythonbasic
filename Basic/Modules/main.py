
import builtins
from pprint import pprint
import os

path = "C:\\Users\\amink\\Documents\\src\\koljitechs-pythonbasic\\Basic\\Modules"
pprint(dir(os.path))
# print(os.path.basename(path))
# print(os.path.getsize(path))
# print(os.path.getctime(path)) # get date, year, month, day
# print(os.path.exists(path))
# print(os.path.expanduser(path))
# print(os.path.isdir(path))
# print(os.path.isfile(path))
#print(os.path.ismount(path))
#print(os.path.jion(path, path2 ))
#print(os.path.realpath(path))
'''
path = "C:\\Users\\amink\\Documents\\src\\koljitechs-pythonbasic\\Basic\\Modules"

if os.path.isfile(path):
    print(os.path.realpath(path))
    prin
elif os.path.isfile(path):
    print()
else:
    print("")
    
'''
#creating directory with 
#print(os.mkdir("kojitechs"))
# king = ["ab", "cf"]
# for i in king:
#     #os.mkdir(i)
#     os.removedirs(i)
# print(os.listdir(path))
# print(os.listdir())

print(os.mkdir("platform-modules"))

print(os.mkdir("Datetime-modules"))