FROM debian:stretch-slim

ARG GRAFANA_URL="https://dl.grafana.com/oss/release/grafana_5.3.4_armhf.deb"
ARG GF_UID="472"
ARG GF_GID="472"

ENV PATH=/usr/share/grafana/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    GF_PATHS_CONFIG="/etc/grafana/grafana.ini" \
    GF_PATHS_DATA="/var/lib/grafana" \
    GF_PATHS_HOME="/usr/share/grafana" \
    GF_PATHS_LOGS="/var/log/grafana" \
    GF_PATHS_PLUGINS="/var/lib/grafana/plugins" \
    GF_PATHS_PROVISIONING="/etc/grafana/provisioning"

RUN apt-get update && apt-get install -qq -y tar libfontconfig wget ca-certificates && \
    mkdir -p "$GF_PATHS_HOME/.aws" && \
    wget "$GRAFANA_URL" && \
    dpkg -i grafana_5.3.4_armhf.deb && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*
    #groupadd -r -g $GF_GID grafana && \
    #useradd -r -u $GF_UID -g grafana grafana && \
    #mkdir -p "$GF_PATHS_PROVISIONING/datasources" \
    #         "$GF_PATHS_PROVISIONING/dashboards" \
    #         "$GF_PATHS_LOGS" \
    #         "$GF_PATHS_PLUGINS" \
    #         "$GF_PATHS_DATA" && \
    #cp "$GF_PATHS_HOME/conf/sample.ini" "$GF_PATHS_CONFIG" && \
    #cp "$GF_PATHS_HOME/conf/ldap.toml" /etc/grafana/ldap.toml && \
    #chown -R grafana:grafana "$GF_PATHS_DATA" "$GF_PATHS_HOME/.aws" "$GF_PATHS_LOGS" "$GF_PATHS_PLUGINS" && \
    #chmod 777 "$GF_PATHS_DATA" "$GF_PATHS_HOME/.aws" "$GF_PATHS_LOGS" "$GF_PATHS_PLUGINS"

EXPOSE 3000

#COPY ./run.sh /run.sh

USER grafana
WORKDIR /
ENTRYPOINT [ "grafana" ]