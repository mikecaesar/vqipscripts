#############################################
# Utilities used by the various scripts
# 
# Version 0.1 - 12th July 2017 - Mike Caesar
# Version 0.3 - 26th July 2017 - Mike Caesar
#               Added Logging and -v option
# Version 0.4 - 15th Aug 2017 - Mike Caesar
#               Updated logging to include username
#############################################

#!/usr/bin/python
import json
import requests
import getpass
import os
import sys
import logging
from config import *

# Configure Logging
nameofuser=getpass.getuser()
extra = {'username':nameofuser}
logger = logging.getLogger(__name__)
handler = logging.FileHandler('/var/log/vqipscripts.log')
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(filename)s:%(username)s - %(message)s')
handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger = logging.LoggerAdapter(logger, extra)

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
    try:
        r = requests.post(loginurl, headers=headers, verify=False, data=data)
        return r.headers.get('authentication')
    except requests.ConnectionError as errmessage:
        print(errmessage)
        logger.error('Token Request Failed with : %s' %(errmessage))
        sys.exit(1)

def chkstatus(code,content,fail='yes'):
    if (code == 200 or code == 201):
        print('Success')
    else:
        print('Failed:')
	print(content)
        logger.error(content)
        if fail == 'yes':
            sys.exit(1)

