FROM resin/raspberrypi3-python:3

# Setup external package-sources
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    snmp \
    snmpd \
    --no-install-recommends && \ 
    curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add - && \
    echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list  && \
    apt-get update && apt-get install -y \
    telegraf \
    --no-install-recommends && \
    apt-get remove --auto-remove -y \
    apt-transport-https && \
    rm -rf /var/lib/apt/lists/*

RUN pip install speedtest-cli  && \
    pip install evohomeclient

COPY ./mibs /usr/share/snmp/mibs
COPY ./evohome.py /usr/app/evohome.py
COPY ./telegraf.conf /etc/telegraf/telegraf.conf
COPY ./octopus.py /usr/app/octopus.py
COPY ./weather.py /usr/app/weather.py
RUN chmod ugo+rx /usr/app/evohome.py
RUN chmod ugo+rx /usr/app/octopus.py
RUN chmod ugo+rx /usr/app/weather.py

RUN chmod ugo+r /usr/share/snmp/mibs

CMD ["telegraf"]
