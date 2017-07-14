#!/usr/bin/python
import json
import requests
import getpass
import os
import sys
from config import *

# Get a token. The argument defines the expiry time in seconds. Defaults to 20.
def get_token(exp=20):
    # Prompt for the password if it isn't set in config
    # Use getpass so that password is not displayed as it is typed
    global adminpass
    try:
        adminpass
    except NameError:
        adminpass = getpass.getpass('Enter the password for the qipman admin user : ')
    # Get a token  
    headers = {'Content-Type': 'application/json'}
    data = "{\"username\" : \"qipman\",\"password\": \"" + adminpass + "\",\"expires\": " + str(exp) + "}"
    
    # loginurl comes from config imported above
    r = requests.post(loginurl, headers=headers, verify=False, data=data)
    return r.headers.get('authentication')

def chkstatus(code,content,fail='yes'):
    if (code == 200 or code == 201):
        print('Success')
    else:
        print('Failed:')
	print(content)
        if fail == 'yes':
            sys.exit(1)
