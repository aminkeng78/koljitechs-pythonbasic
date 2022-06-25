
#working with this file
import json, os

# file_name = "parameters.json"
# #if os.path.exists(file_name):
#     #print(f"{file_name} already exists")
# with open(file_name, "r") as file:
#     data = file.read()
#     print(data)
    
''' 
file_name = {'Name': {"First_Name": "Bello", "LastName": "koji", "Middle_name": ''},
            "Skills": ['Python', "Terraform", "cdk", "java script", "html" 'Ansible', ]          
}
#json.dump() method(without "s" in dump) used to write python objects  (serianlized)
with open("loaduserinfor.json", "w") as file:
    json.dump(file_name, file, indent=4)

with open("loaduserinfor.json", "r") as file:
    data = file.read()
    print(data)
'''   
file_name = {'Name': {"First_Name": "Bello", "LastName": "koji", "Middle_name": "", "is_male":"True"},
            "Skills": ['Python', "Terraform", "cdk", "java script", "html" 'Ansible', ]          
}

    
    
#json.dumps() this will write json string format
with open("loaduserinfor.json", "r") as file:
   data = json.dumps(file_name, indent=4,)
   print(data)