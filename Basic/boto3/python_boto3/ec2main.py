
import boto3
from pprint import pprint

from click import option
import time

#client = boto3.session.Session().client('ec2', 'us-east-1')

resource = boto3.session.Session().resource('ec2', 'us-east-1')

#pprint(dir(client))

def describe_instance_clients():
    """this list  all instances using object
    parameter : None
    Return : None
    """
    client = boto3.session.Session().client('ec2', 'us-east-1')
    response =client. describe_instances()['Reservations']
    for instance in response:
        for each_instance in instance['Instances']:
            pprint("==========================")
            print(f"Instance_id: {each_instance.get('InstanceId')}\nLaunchTime is: {each_instance.get('LaunchTime').strftime('%y-%m-%d')}\nInstance Status: {each_instance.get('State').get('Name')}")

        
    
    
#describe_instance_clients()     

## Describe instances using resource objects

def describe_instance_resource():
    """this list  all instances using resource object.
    parameter : None
    Return : None
    """
    instance_ids = []
    resource = boto3.session.Session().resource('ec2', 'us-east-1')
    response = resource.instances.all()
    for each_instance in response:
        instance_ids.append(each_instance.id)
    print(instance_ids)
    return instance_ids

instance_ids = describe_instance_resource()
#print(instance_ids)


### USING CLIENT OBJECT TO STOP OR START AN INSTANCE

def stopping_instance_cli():
    """this list  all instances using resource object.
    parameter : None
    Return : None
    """
    client = boto3.session.Session().client('ec2', 'us-east-1')
    print("stoping all the instances ...........")
    client.stop_instances(InstanceIds=instance_ids)
    print("instances stopped ...........")
    return None
    

#stopping_instance_cli()

def starting_instance_cli(ids):
    """this list  all instances using resource object.
    parameter : None
    Return : None
    """
    client = boto3.session.Session().client('ec2', 'us-east-1')
    print("starting all the instances ...........")
    client.start_instances(InstanceIds=ids)
    print("starting instances ...........")
    return None
    

#starting_instance_cli(instance_ids)


def melo_driven_script():
    """This is to perform actionlike terminate, stop,start, and exitbase on user
    parameter : opt(int)
    Return : None
    """
    client = boto3.session.Session().client('ec2', 'us-east-1')
    print("""
          1. Start
          2. Stop
          3. terminate
          4. Exit
          """)
    option = int(input("please select your option list"))
    if option ==1:
         print("starting all the instances ...........")
         client.start_instances(InstanceIds=instance_ids)
         time.sleep(20)
         print("started instances ...........")
    elif option ==2:
        print("stoping all the instances ...........")
        client.stop_instances(InstanceIds=instance_ids)
        time.sleep(20)
        print("instances stopped ...........")
    elif option ==3:
         print("terminating all the instances ...........")
         client.terminate_instances(InstanceIds=instance_ids)
         time.sleep(40)
         print("instances terminter ...........")
    elif option ==4:
        print("exit")
        
    else:
        print(f"{option} is invalid. please providea valid option and try again")
        return None
    
melo_driven_script()
         
        