# Pull base image
FROM resin/rpi-raspbian:stretch
MAINTAINER Henrik Östman <trycoon@gmail.com>

# Setup external package-sources
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    --no-install-recommends && \ 
    curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add - && \
    echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list  && \
    apt-get update && apt-get install -y \
    influxdb \
    --no-install-recommends && \
    apt-get remove --auto-remove -y \
    apt-transport-https && \
    rm -rf /var/lib/apt/lists/*

#COPY influxdb.conf /etc/influxdb/influxdb.conf


