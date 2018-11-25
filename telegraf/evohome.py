#!/usr/local/bin/python
from evohomeclient import EvohomeClient

evoclient = EvohomeClient('info@grimjak.org.uk', 'Val1n0rho')

for device in evoclient.temperatures():
    if device["thermostat"]=="DOMESTIC_HOT_WATER":
      print ("evohome,room=hotwater temperature="+str(device["temp"]))
    else:
      print ("evohome,room="+device["name"].translate(str.maketrans({" ": "\ "}))+" temperature="+str(device["temp"])+",setpoint="+str(device["setpoint"]))
