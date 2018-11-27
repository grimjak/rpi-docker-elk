#!/usr/local/bin/python3
import datetime

import requests
timefrom = (datetime.datetime.now()-datetime.timedelta(hours=24)).isoformat()
contents = requests.get("https://api.octopus.energy/v1/electricity-meter-points/1012477457919/meters/17P1073309/consumption/", auth=('sk_live_qbE5sgjysVRpmEaPCY7LmfCP', '')).json()
timestampstr = contents['results'][0]['interval_end']
timestamp = datetime.datetime.strptime(timestampstr, "%Y-%m-%dT%H:%M:%SZ")
consumption = contents['results'][0]['consumption']

print('energy,type=electricity consumption='+str(consumption)+' '+str(int(1e9*timestamp.timestamp())))
