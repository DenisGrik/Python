#!/usr/bin/env python3

import socket
import json
import sys

argLen=len(sys.argv)
if argLen==1:
    sys.exit()

City=sys.argv[2]
APPID=sys.argv[1]

for i in range(len(sys.argv)-3):    #Cities with more than 1 word
    City=City+'%20'+sys.argv[i+3]

HOST = 'api.openweathermap.org'
PORT = 80


msg="GET /data/2.5/weather?q=" +City+ "&APPID=" +APPID+ "&units=metric HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"
bmsg=str.encode(msg) #string to bit object

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creating socket
    s.connect((HOST, PORT)) # connect to api
    s.sendall(bmsg) #get request
    data = s.recv(1024)

data=repr(data)
if '404 Not Found' in data:
    print ('Wrong city name')
    sys.exit()

if '401 Unauthorized' in data:
    print ('Wrong API key')
    sys.exit()

x=data.find('{"coord')
y=data.find("'",10)
data=data[x:y] #cutting string
jsonData=json.loads(data)

City=City.replace("%20"," ")
print (City)
for weather in jsonData['weather']:
    print (weather['description'])

if 'temp' in data:
    print ("temp:",jsonData['main']['temp'],"Degrees Celsius")
if 'humidity' in data:
    print ("humidity:",jsonData['main']['humidity'],"%")
if 'pressure' in data:
    print ("pressure:",jsonData['main']['pressure'],"pHa")
if 'wind-speed' in data:
    print ("wind-speed:",jsonData['wind']['speed'],"km/h")
if 'wind-deg' in data:
    print ("wind-deg:",jsonData['wind']['deg'])
