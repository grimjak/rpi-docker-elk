#!/usr/bin/env bash

# Wait for the Elasticsearch container to be ready before starting Kibana.
echo "Stalling for Elasticsearch"
while true; do
    nc -q 1 192.168.1.204 9200 2>/dev/null && break
done

echo "Starting Kibana"
exec kibana
