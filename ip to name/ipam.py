#! /bin/python3
import os
import requests
import sys

if os.getenv('IPAM_TOKEN')=='None':
    print('please set your ipam api token as an env named IPAM_TOKEN')
    exit(0)
if len(sys.argv) < 3 :
    print('please enter your ip file a the first arg and your domin as the second one ')
    exit(0)
token = os.getenv('IPAM_TOKEN')
file = open(sys.argv[1], 'r')
responses = []
ips = file.read().splitlines()
for ip in ips :
    auth_header='Token {APITOKEN}'.format(APITOKEN=token)
    uri='https://{DOMIN}/api/ipam/ip-addresses'.format(DOMIN=sys.argv[2])
    response = requests.get(
        'https://ipam.partdp.ir/api/ipam/ip-addresses',
        params={'q': ip},
        headers={ 'content-type': 'application/json' , 'Authorization' : auth_header },
    ) 
    res=[ip,response.json()]
    responses.append(res)
for res in responses:
    print(res[0],res[1]['results'][0]['assigned_object']['virtual_machine']['name'])
