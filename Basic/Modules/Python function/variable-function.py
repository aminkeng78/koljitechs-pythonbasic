'''
def sum(arg1, arg2):
    """_summary_
    this function sum up two exected arguments.

    """
    total = arg1 + arg2
    print("we are insite the body")
    return total

response = sum(2,3)
print(response)
'''

def add(arg1, arg2):
    """_summary_
    this function sum up two exected arguments.

    """
    global sum_of;
    sum_of =30
    print("we are insite the body.")
    #return sum_of 
def main(b):
    c = sum_of + b
    print(c)

add()
main(12)    

