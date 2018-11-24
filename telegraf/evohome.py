#!/usr/local/bin/python
import sys
#from influxdb import InfluxDBClient
from evohomeclient import EvohomeClient

#client = InfluxDBClient('192.168.1.204',8086,'root','root','telegraf')

evoclient = EvohomeClient('info@grimjak.org.uk', 'Val1n0rho')

#time = int(time.time())


for device in evoclient.temperatures():
    if device["thermostat"]=="DOMESTIC_HOT_WATER" :
      print ("evohome,room=hotwater temperature="+str(device["temp"]))
    else:
      print ("evohome,room="+device["name"].translate(str.maketrans({" ":"\ "}))+" temperature="+str(device["temp"])+",setpoint="+str(device["setpoint"]))
