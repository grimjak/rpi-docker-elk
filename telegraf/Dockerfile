FROM arm32v7/telegraf:latest

RUN apt-get update && apt-get install -y python-pip && \
    pip install speedtest-cli

COPY ./mibs /usr/share/snmp/mibs
COPY ./evohome.py /usr/app/evohome.py

CMD ["telegraf"]
