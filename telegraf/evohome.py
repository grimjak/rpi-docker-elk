#!/usr/bin/python
import sys
#from influxdb import InfluxDBClient
from evohomeclient import EvohomeClient

#client = InfluxDBClient('192.168.1.204',8086,'root','root','telegraf')

evoclient = EvohomeClient('info@grimjak.org.uk', 'Val1n0rho')

jsonbody = []
#time = int(time.time())
for device in evoclient.temperatures():

    if device["thermostat"]=="DOMESTIC_HOT_WATER" :
      m = {
        "measurement": "temperature",
        "tags" :{
          "room": "Hot water",
          "sensor": "1"
        },
        "fields": {
          "value": device["temp"]
        },
      }
      jsonbody.append(m)
    else:
      m = {
        "measurement": "temperature",
        "tags" :{
          "room": device["name"],
          "sensor": "1"
        },
        "fields": {
          "value": device["temp"]
        }
      }
      jsonbody.append(m)
      m = {
        "measurement": "setpoint",
        "tags" :{
          "room": device["name"],
          "sensor": "1"
        },
        "fields": {
          "value": device["setpoint"]
        }
      }
    jsonbody.append(m)

#switch to outputing json to run this in telegraf
#client.write_points(jsonbody)
print(jsonbody)