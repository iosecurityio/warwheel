#!/bin/bash

# check internet
# refactor to other pc
ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null && echo Internet Up || echo No Internet; exit

# Install Wifi Stuff
# https://www.kismetwireless.net/docs/readme/config_files/
wget -O - https://www.kismetwireless.net/repos/kismet-release.gpg.key | sudo apt-key add -
echo 'deb https://www.kismetwireless.net/repos/apt/release/kali kali main' | sudo tee /etc/apt/sources.list.d/kismet.list
sudo apt-get update
sudo apt-get install gpsd-clients gpsd kismet build-essential git libwebsockets-dev pkg-config zlib1g-dev libnl-3-dev libnl-genl-3-dev libcap-dev libpcap-dev libnm-dev libdw-dev libsqlite3-dev libprotobuf-dev libprotobuf-c-dev protobuf-compiler protobuf-c-compiler libsensors4-dev libusb-1.0-0-dev python3 python3-setuptools python3-protobuf python3-requests python3-numpy python3-serial python3-usb python3-dev python3-websockets librtlsdr0 libubertooth-dev libbtbb-dev -y
sudo apt-get upgrade -y


sudo usermod -a -G kismet pi
sudo mkdir /var/log/kismet
sudo chmod 777 /var/log/kismet
sudo nano /usr/local/etc/kismet.conf

#Fedora
#sudo dnf install make automake gcc gcc-c++ kernel-devel git libwebsockets-devel pkg-config zlib-devel libnl3-devel libcap-devel libpcap-devel NetworkManager-libnm-devel libdwarf libdwarf-devel elfutils-devel libsqlite3x-devel protobuf-devel protobuf-c-devel protobuf-compiler protobuf-c-compiler lm_sensors-devel libusb-devel fftw-devel gpsd kismet gpsd-clients -y

#http://www.intellamech.com/RaspberryPi-projects/rpi3_kismet.html
# https://stackoverflow.com/questions/17291233/how-can-i-check-internet-access-using-a-bash-script-on-linux

# place nic in monitor mode
# check gps 
# place gps in active mode
# start kismet or whatever you are going to use to snarf