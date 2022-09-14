#!/bin/bash

# If there is an output here, you are good to go
sudo stty -F /dev/ttyUSB0 ispeed 4800 && sudo cat </dev/ttyUSB0

# Else GPS isnt started
# Ensure Plugged in adapter
# sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock

# If all else fails:
# sudo killall gpsd
# sudo rm /var/run/gpsd.sock
# Go back to step 1

# cgps / xgps for checks