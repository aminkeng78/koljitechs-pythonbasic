
import boto3

session = boto3.session.Session()
client = session.client('sts')
'''
def get_account_id():
    """This function print account ID account arn
    Parameter: None
    Return None
    """
    
    try:
        client = session.client('sts')
        response = client.get_caller_identity()
        print(f"my account ID is :{response.get('Account')}\nAccount arn: {response.get('Arn')}")
        
    except Exception as err:
        print(err)
    return None
        
get_account_id()      
'''

#USING BOTO3 TO WORK WITH IAM AND

resource = session.resource('iam')  # this  is global
client = session.client('iam')    # this  is global

def list_roleWithClien():
    """this list all available roles with client.com
    Parameter: None
    Return: None
    """
    try: 
      response = client.list_roles()['Role']
      for role in response:
          print(f"Role arn: {role.get('Arn')}\nRole Name: {role.get('RoleName')}\nRole Description: {role.get('Description')}")
    except Exception as err:
      print(err)
    return None


list_roleWithClien()


##### Exception handling with boto3
try:
    boto3

except Exception as e:
    print(e)