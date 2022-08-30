#!/bin/bash

# check nic
# place nic in monitor mode
# check gps 
# place gps in active mode
# start kismet or whatever you are going to use to snarf

sudo apt-get update
sudo apt-get upgrade -y
# Install Wifi Stuff
# https://www.kismetwireless.net/docs/readme/config_files/
wget -O - https://www.kismetwireless.net/repos/kismet-release.gpg.key | sudo apt-key add -
echo 'deb https://www.kismetwireless.net/repos/apt/release/kali kali main' | sudo tee /etc/apt/sources.list.d/kismet.list
sudo apt-get update
sudo apt-get install kismet -y
# Install GPS Stuff
sudo apt-get install gpsd

# https://stackoverflow.com/questions/17291233/how-can-i-check-internet-access-using-a-bash-script-on-linux