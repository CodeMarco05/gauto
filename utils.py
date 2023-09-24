import datetime
import json
import os.path
import sys


# Get the path to the directory containing the script
script_dir = os.path.dirname(sys.argv[0])

# Construct the path to config.json relative to the script's directory
CONFIGFILEPATH = os.path.join(script_dir, "config.json")

def get_default_push_message():
    with open(CONFIGFILEPATH, 'r') as file:
        data = json.load(file)
        if data['push-default-message'] == 'timestamp':
            return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        else:
            return str(data['push-default-message'])

def get_default_push_branch():
    with open(CONFIGFILEPATH, 'r') as file:
        data = json.load(file)
        return data['branches'][0]['push-default-branch']

def get_default_pull_branch():
    with open(CONFIGFILEPATH, 'r') as file:
        data = json.load(file)
        return data['branches'][0]['pull-default-branch']