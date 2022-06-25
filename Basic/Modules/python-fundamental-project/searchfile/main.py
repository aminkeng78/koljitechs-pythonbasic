
import os
import sys
import platform

def search_file(filename):
    """This search is use to search a ny file provided by user and display entire file path
    Paramater: int
    Return:
    None
    """
    file = os.walk("C:\\Users\\amink")
    for r,d,f in file:
        for each_file in f:
            if each_file == filename:
                print(os.path.join(r, each_file))
                print(sys.exit())
'''
filename=input("what is the file you are searching for?:")

search_file(filename)
'''        
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    return None
        
        
clear_screen()