#!/usr/bin/env python3.12

##
# A Python script to create and manage Amazon EC2 instances.
##

# Import community modules.
import os
import sys
import time
import boto3

# Only allow vagrant user to execute this script.
if os.geteuid()==1000:
  time.sleep(1)
else:
  print('Please run this script as vagrant user.')
  sys.exit(1)

# Set AWS profile.
AWS_PROFILE = 'tuto'

# Initialize Amazon EC2 client.
session = boto3.Session(profile_name=AWS_PROFILE)
client = session.client('ec2')

# Create Amazon EC2 instance.
def create():
  print('Not yet completed...')

# Start Amazon EC2 instance.
def start(id):
  print('Starting Amazon EC2 instance...')
  client.start_instances(InstanceIds=[id])
  print('Done.')

# Stop Amazon EC2 instance.
def stop(id):
  print('Stopping Amazon EC2 instance...')
  client.stop_instances(InstanceIds=[id])
  print('Done.')

# Terminate Amazon EC2 instance.
def terminate():
  print('Not yet completed...')


# Choose an Amazon EC2 instance operation.
if sys.argv[1]=='start':
  start(sys.argv[2])
elif sys.argv[1]=='stop':
  stop(sys.argv[2])
elif sys.argv[1]=='terminate':
  terminate()
else:
  print('Please provide proper CLI arguments.')
  sys.exit(1)
 