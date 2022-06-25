
from pprint import pprint
from datetime import datetime
import time
#pprint(dir(datetime))
pprint(dir(time))
# print(datetime.now)
# print(datetime.today)
# print(datetime.year)
#tim = datetime.now()
#print(tim.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.minute)
# print(time.month)
# print(time.hour)
def hello(name):
    print(f"Good morning and welcome {name}")
    time.sleep(5)
    print(f"Good morning and welcome {name}")
hello("koji")
hello("philo")