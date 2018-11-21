FROM arm32v7/telegraf:latest

RUN apt-get install -y speedtest-cli
COPY ./mibs /usr/share/snmp/mibs
COPY ./evohome.py /usr/app/evohome.py

CMD ["telegraf"]
