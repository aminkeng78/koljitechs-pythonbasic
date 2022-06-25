
import csv
#working with csv (comma sep value)
# firstName last_name data_of_birth
'''
req_file = input("PLEASE ENTER FILE PATH")
#Opening csv is a writemode.
with open(req_file, "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["DATE", "TOPIC", "VIDEO"])
    csv_writer.writerow(["TuesDay-10-05-2022", "introduction" ])
  
# req_file = input("Enter the file name ")
# with open(req_file, "r") as file:
#     data = csv.reader(file)
#     print(data)
    
header = ["name ","area", "country_code2", "country_code3"]
data = [
    ["albain", "28748", "Al", "Alb"],
    ["Algeria", "2381741", "Az", "Dza"],
    ["american samoa", "199", "As", "Asm"]
    
]
with open("address.csv", "w") as file:
    csv_writer= csv.writer(file)
    
     # we have to write those data in a csv file
    #print(dir(csv_writer))
    # writerow  is just to write one list 
    csv_writer.writerow(header)
    #writer mutiple rows we use writerows
    csv_writer.writerow(data)
    
    
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    {"name": "Alabama", "area": 25678, "country_code2": "alb", "country_code3": "ABSHD"},
    {'name': 'Algeria', 'area': 2381741, 'country_code2': 'DZ','country_code3': 'DZA'},
    {'name': 'American Samoa', 'area': 199, 'country_code2': 'AS','country_code3': 'ASM'}
]

with open("address2.csv", "w") as file:
    # pprint(dir(csv))
    # 
    writer_csv = csv.DictWriter(file, fieldnames=header)
    # pprint(dir(writer_csv))
    writer_csv.writeheader()

    writer_csv.writerows(data)
'''    
header = ["DATE", "TOPIC", "VIDEO"]
data = [
    ["11/5/22", "intro/instLL", "CLICK"],
    ["13/5/22", "CONDI","CLICK"]
    
]