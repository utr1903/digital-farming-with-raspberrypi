#!/usr/bin/bash

echo Y | sudo apt-get install python3 idle3 python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel --break-system-packages
