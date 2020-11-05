import boto3
import time

##
# First function will try to filter for EC2 instances that contain a tag named `Scheduled` which is set to `True`
# If that condition is meet function will compare current time (H:M) to a value of the additional tags which defines the trigger `ScheduleStop` or `ScheduleStart`.
# Value of the `ScheduleStop` or `ScheduleStart` must be in the following format `H:M` - example `09:00`  
# 
# In order to trigger this function make sure to setup CloudWatch event which will be executed every minute. 
# Following Lambda Function needs a role with permission to start and stop EC2 instances and writhe to CloudWatch logs.
# Copy by https://gist.githubusercontent.com/gregarious-repo/b75eb8cb34e9b3644542c81fa7c7c23b/raw/4f692e5e4ce7bb674706e7b87dcc4d5a08928087/lambda_function.py
# 
# Example EC2 Instance tags: 
# 
# Scheduled     : True
# ScheduleStart : 06:00
# ScheduleStop  : 18:00
# Time format UTC
# Using Python 3.6
##

#define boto3 the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
    # Get current time in format H:M
    current_time = time.strftime("%H:%M")
    
    # Find all the instances that are tagged with Scheduled:True
    filters = [{
            'Name': 'tag:Scheduled',
            'Values': ['True']
        }
    ]

    # Search all the instances which contains scheduled filter 
    instances = ec2.instances.filter(Filters=filters)

    stopInstances = []   
    startInstances = []   

    # Locate all instances that are tagged to start or stop.
    for instance in instances:
            
        for tag in instance.tags:

            if tag['Key'] == 'ScheduleStop':

                if tag['Value'] == current_time:

                    stopInstances.append(instance.id)

                    pass

                pass

            if tag['Key'] == 'ScheduleStart':

                if tag['Value'] == current_time:

                    startInstances.append(instance.id)

                    pass

                pass

            pass

        pass
    
    print (current_time)
    
    # shut down all instances tagged to stop. 
    if len(stopInstances) > 0:
        # perform the shutdown
        stop = ec2.instances.filter(InstanceIds=stopInstances).stop()
        print (stop)
    else:
        print ("No instances to shutdown.")

    # start instances tagged to stop. 
    if len(startInstances) > 0:
        # perform the start
        start = ec2.instances.filter(InstanceIds=startInstances).start()
        print (start)
    else:
        print ("No instances to start.")
