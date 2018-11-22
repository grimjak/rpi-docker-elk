FROM FROM resin/raspberry-pi-alpine-python:3

# Setup external package-sources
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    --no-install-recommends && \ 
    curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add - && \
    echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list  && \
    apt-get update && apt-get install -y \
    telegraf \
    --no-install-recommends && \
    apt-get remove --auto-remove -y \
    apt-transport-https && \
    rm -rf /var/lib/apt/lists/*

RUN pip install speedtest-cli && \
    pip install evohome-client

COPY ./mibs /usr/share/snmp/mibs
COPY ./evohome.py /usr/app/evohome.py
COPY ./telegraf.conf /etc/telegraf/telegraf.conf

CMD ["telegraf"]
