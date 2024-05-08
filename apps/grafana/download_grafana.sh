#!/usr/bin/bash

wget https://dl.grafana.com/enterprise/release/grafana-enterprise-10.4.2.linux-arm64.tar.gz
tar -zxvf grafana-enterprise-10.4.2.linux-arm64.tar.gz
sudo rm -r grafana-enterprise-10.4.2.linux-arm64.tar.gz
sudo mv ./grafana-v10.4.2 ./grafana