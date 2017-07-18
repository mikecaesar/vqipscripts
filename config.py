esmhost = 'vqip'
esmport = '8080'
org = 'VitalQIP%20Organization'
domain = 'example.domain.com'
adminpass = 'qipman'
# Following option is used only by registerIpFile.
# This should be a comma separated list of any subnets that might be in
# the csv file, but should be ignored and not registered. This would be
# used for example for dual NIC hosts where only one NIC needs to be registered
# with VitalQIP.
# Example:
#ignore_subnets = '192.168.17.0,172.17.0.0,103.30.185.224'
ignore_subnets = ''

# Do not change items below here
apiurl = 'http://' + esmhost + ':' +esmport + '/api/v1/' + org 
loginurl = 'http://' + esmhost + ':' +esmport + '/api/login'
