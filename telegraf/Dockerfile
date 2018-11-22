FROM arm32v7/telegraf:latest

<<<<<<< HEAD
RUN apt-get update && apt-get install -y python-pip --no-install-recommends && \
    pip install speedtest-cli
=======
RUN apt-get update && apt-get install -y python-pip && \
    pip install speedtest-cli && \
    pip install evohome-client
>>>>>>> 710c3f64759bf21c577b893ae3a4c40646970ff6

COPY ./mibs /usr/share/snmp/mibs
COPY ./evohome.py /usr/app/evohome.py
COPY ./telegraf.conf /etc/telegraf/telegraf.conf

CMD ["telegraf"]
