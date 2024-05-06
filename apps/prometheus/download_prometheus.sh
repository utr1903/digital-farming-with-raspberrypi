#!/usr/bin/bash

wget https://github.com/prometheus/prometheus/releases/download/v2.51.2/prometheus-2.51.2.linux-arm64.tar.gz
tar -xvf prometheus-2.51.2.linux-arm64.tar.gz
sudo mv ./prometheus-2.51.2.linux-arm64/prometheus ./prometheus
sudo rm -r prometheus-2.51.2.linux-arm64*
