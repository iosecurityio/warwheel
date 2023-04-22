# warwheel.py

## Overview

Warwheel is a project that enables the rider of a Personal Electric Vehicle (PEV) to Wardrive, hence "warwheel".

In my case, I will share my setup and configuration files that I use in a Sling pack while floating on a Onewheel.

> Always wear your helmet! 🪖

## Usage

1. `chmod +x ./bootstrap_warwheel.sh`

1. `./bootstrap_warwheel.sh`

## Project Structure

```python
warwheel
├── conf
│   └── kismet.conf
├── docs
├── README.md
├── requirements.txt
├── scripts
│   ├── bootstrap_warwheel.sh
│   ├── start-kismet.sh
│   └── troubleshoot-gps.sh
├── src
│   ├── __init__.py
│   └── warwheel.py
└── tests
    └── tests.py

6 directories, 9 files
```

## References

- https://github.com/kismetwireless/python-kismet-rest

- http://www.intellamech.com/RaspberryPi-projects/rpi3_kismet.html

- https://stackoverflow.com/questions/17291233/how-can-i-check-internet-access-using-a-bash-script-on-linux

- https://www.python-httpx.org/
