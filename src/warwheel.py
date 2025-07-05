# Warwheel v0.0.1b
# Created by: Allen Montgomery <allen@iosecurity.io>
# https://github.com/iosecurityio/warwheel
# Portable War Driving Tool
# -*- coding: utf-8 -*-

import os
from datetime import datetime

import httpx
import kismet_rest
from colorama import init, Fore
from dotenv import load_dotenv

init(autoreset=True)  # initialize colarama


class Warwheel:
    """Creates a warwheel object"""

    def __init__(self):
        self.start_time = ""
        self.start_date = ""
        self.start_location = ""
        self.internet = False
        self.bluetooth = False
        self.gps = False
        self.kismet = False
        self.KISMET_USER = ""
        self.KISMET_PASS = ""
        self.KISMET_API_KEY = ""
        self.WIGLE_API_KEY = ""
        self.end_time = ""
        self.end_date = ""

        self.splash()
        self.start()

    def splash(self):
        print(Fore.LIGHTGREEN_EX + """
__        __        """ + Fore.GREEN + """          _               _ """ + Fore.LIGHTGREEN_EX + """
\ \      / /_ _ _ __""" + Fore.GREEN + """__      _| |__   ___  ___| |""" + Fore.LIGHTGREEN_EX + """
 \ \ /\ / / _` | '__""" + Fore.GREEN + """\ \ /\ / / '_ \ / _ \/ _ \ |""" + Fore.LIGHTGREEN_EX + """
  \ V  V / (_| | |  """ + Fore.GREEN + """ \ V  V /| | | |  __/  __/ |""" + Fore.LIGHTGREEN_EX + """
   \_/\_/ \__,_|_|  """ + Fore.GREEN + """  \_/\_/ |_| |_|\___|\___|_|""")
        print("Name: warwheel.py v0.0.1b")
        print("Author: allen@iosecurity.io")
        print("Source: https://github.com/iosecurityio/warwheel")
        print("-" * 64)

    def start(self):
        try:
            load_dotenv()
            self.KISMET_USER = os.getenv("KISMET_USER")
            self.KISMET_PASS = os.getenv("KISMET_PASS")
            self.KISMET_API_KEY = os.getenv("KISMET_API_KEY")
            self.WIGLE_API_KEY = os.getenv("WIGLE_API_KEY")
            print("[*] Environment Loaded!")
        except Exception as e:
            print(f"Exception when loading environment: {e}")

        now = datetime.now()
        self.set_start_time(now.strftime("%H:%M:%S"))
        self.set_start_date(now.strftime("%m-%d-%Y"))
        self.check_internet()
        self.check_bluetooth()
        self.check_gps()
        self.get_location()
        self.start_location = "get location from gps"

    def check_internet(self):
        try:
            print("[*] Checking Internet Connection...")
            with httpx.Client() as client:
                r = client.get("https://www.google.com")
                if r.status_code == 200:
                    self.internet = True
                    print(Fore.GREEN + "[*] Internet Connection: OK")
                else:
                    self.internet = False
                    print(Fore.RED + "[X] Internet Connection: DOWN")
        except Exception as e:
            print(f"[X] Error checking Internet Connection: {e}")

    def check_bluetooth(self):
        try:
            print("[*] Checking Bluetooth...")

        except Exception as e:
            print(Fore.RED + f"[X] Error checking Bluetooth: {e}")

    def check_gps(self):
        try:
            print("[*] Checking GPS...")
        except Exception as e:
            print(Fore.RED + f"[X] Error checking GPS: {e}")

    def get_location(self):
        if not self.gps:
            print(Fore.RED + "[X] GPS is not enabled.")
            return
        try:
            print("[*] Getting Location...")
        except Exception as e:
            print(Fore.RED + f"[X] Error getting Location: {e}")

    def check_kismet(self):
        print("[*] Checking Kismet...")
        try:
            devices = kismet_rest.Devices()
            for device in devices.all(ts=1546300800):
                print(device)
        except Exception as e:
            print(Fore.RED + f"[X] Error connecting to Kismet: {e}")

    def upload_scan(self, file):
        """Upload a scan to WiGLE.net via the API
        :param file: The file to upload

        Reference: https://api.wigle.net/swagger#/Network%20observation%20file%20upload%20and%20status./upload
        """

        try:
            headers = {"Authorization": f"Bearer {self.WIGLE_API_KEY}"}
            with httpx.post("https://api.wigle.net/api/v2/file/upload", headers=headers,
                            files={"file": open(file, "rb")}) as r:
                print(r.text)
        except Exception as e:
            print(Fore.RED + f"[X] Error uploading to WiGLE: {e}")

    def shutdown(self):
        # Do any cleanup here
        self.set_end_time(datetime.now().strftime("%H:%M:%S"))
        self.set_end_date(datetime.now().strftime("%m-%d-%Y"))
        print(Fore.LIGHTRED_EX + "[!] Shutting down.")

    def get_start_time(self):
        """Get the start time"""
        return self.start_time

    def set_start_time(self, time):
        """Set the start time"""
        self.start_time = time

    def get_start_date(self):
        """Get the start date"""
        return self.start_date

    def set_start_date(self, date):
        """Set the start date"""
        self.start_date = date

    def get_start_location(self):
        """Get the start location"""
        return self.start_location

    def set_start_location(self, location):
        """Set the start location"""
        self.start_location = location

    def get_internet(self):
        """Get the internet status"""
        return self.internet

    def set_internet(self, status):
        """Set the internet status"""
        self.internet = status

    def get_bluetooth(self):
        """Get the bluetooth status"""
        return self.bluetooth

    def set_bluetooth(self, status):
        """Set the bluetooth status"""
        self.bluetooth = status

    def get_gps(self):
        """Get the GPS status"""
        return self.gps

    def set_gps(self, status):
        """Set the GPS status"""
        self.gps = status

    def get_kismet(self):
        """Get the Kismet status"""
        return self.kismet

    def set_kismet(self, status):
        """Set the Kismet status"""
        self.kismet = status

    def get_end_time(self):
        """Get the end time"""
        return self.end_time

    def set_end_time(self, time):
        """Set the end time"""
        self.end_time = time

    def get_end_date(self):
        """Get the end date"""
        return self.end_date

    def set_end_date(self, date):
        """Set the end date"""
        self.end_date = date


def main():
    """Main function of Warwheel project"""

    # Start it up
    warwheeler = Warwheel()
    print(f"Start Date: {warwheeler.get_start_date()}")
    print(f"Start Time: {warwheeler.get_start_time()}")
    # Shut it down
    warwheeler.shutdown()
    print(f"End Date: {warwheeler.get_end_date()}")
    print(f"End Time: {warwheeler.get_end_time()}")


if __name__ == '__main__':
    main()
