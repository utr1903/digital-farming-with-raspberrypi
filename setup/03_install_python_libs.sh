#!/usr/bin/bash

sudo pip3 install adafruit-circuitpython-dht=4.0.4 Flask=3.0.3 --break-system-packages
echo Y | sudo apt-get install libgpiod2
