#!/bin/bash
sudo stty -F /dev/ttyUSB0 ispeed 4800 && sudo cat </dev/ttyUSB0
# if GPS isnt started
# Ensure Plug in adapter
# sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
# if GPS is started
# sudo killall gpsd
# sudo rm /var/run/gpsd.sock
# Go back to step 1