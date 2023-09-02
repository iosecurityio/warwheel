# warwheel.py v0.0.1c
# Created by: Allen Montgomery <allen@iosecurity.io>
# https://github.com/iosecurityio/warwheel
# Portable War Driving Tool
# -*- coding: utf-8 -*-


from colorama import init, Fore, Back, Style
from datetime import datetime, timedelta
import httpx
import gpsd
import kismet_rest
import os
import sys
from pathlib import Path

kismet_user = ""
kismet_pass = ""
wigle_api_key = ""
kismet_api_key = ""


class WarWheel:
    """Creates WarWheel object to track your warwheeling session.

    Don't forget your helmet!
    """

    def __init__(self):
        self.session_time = {
            "start_date": "",
            "start_time": "",
            "checkpoint": "",
            "end_date": "",
            "end_time": ""
        }
        self.start_location = ""
        self.internet = False
        self.bluetooth = False
        self.gps = False
        self.kismet = False
        self.start()

    def splash(self):
        """Banner for Warwheel."""
        print(Fore.BLUE + Style.DIM + "=" * 33 + Fore.LIGHTBLUE_EX + Style.BRIGHT + "-" * 44)
        print(Fore.BLUE + Style.DIM + """
M""MMM""MMM""M                   """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M""MMM""MMM""M dP                         dP""" + Fore.BLUE + Style.DIM + """ 
M  MMM  MMM  M                   """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  MMM  MMM  M 88                         88""" + Fore.BLUE + Style.DIM + """ 
M  MMP  MMP  M .d8888b. 88d888b. """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  MMP  MMP  M 88d888b. .d8888b. .d8888b. 88""" + Fore.BLUE + Style.DIM + """ 
M  MM'  MM' .M 88'  `88 88'  `88 """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  MM'  MM' .M 88'  `88 88ooood8 88ooood8 88""" + Fore.BLUE + Style.DIM + """
M  `' . '' .MM 88.  .88 88       """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  `' . '' .MM 88    88 88.  ... 88.  ... 88""" + Fore.BLUE + Style.DIM + """
M    .d  .dMMM `88888P8 dP       """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M    .d  .dMMM dP    dP `88888P' `88888P' dP""" + Fore.BLUE + Style.DIM + """
MMMMMMMMMMMMMM                   """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """MMMMMMMMMMMMMM
""")
        print(Fore.BLUE + Style.DIM + "=" * 33 + Fore.LIGHTBLUE_EX + Style.BRIGHT + "-" * 44)
        print("Name: warwheel.py v0.0.1b")
        print("Author: allen@iosecurity.io")
        print("Source: https://github.com/iosecurityio/warwheel")
        print(Fore.BLUE + Style.DIM + "=" * 33 + Fore.LIGHTBLUE_EX + Style.BRIGHT + "-" * 44)

    def start(self):
        """Starts your warwheeling session. """
        try:
            # Prints the splash screen
            self.splash()
            # Sets your starting date and time
            self.session_time["start_date"] = datetime.now().strftime("%m-%d-%Y")
            self.session_time["start_time"] = datetime.now().strftime("%H:%M:%S")
            # Checks your internet connection
            self.check_internet()
            # Checks your bluetooth connection
            self.check_bluetooth()
            # Checks your GPS connection
            self.check_gps()
            # Checks your Kismet connection
            self.check_kismet()
        except Exception as e:
            print(Fore.RED + f"[X] Error starting WarWheel: {e}")

    def end(self):
        """Ends your current warwheeling session. """

        self.session_time["end_date"] = datetime.now().strftime("%m-%d-%Y")
        self.session_time["end_time"] = datetime.now().strftime("%H:%M:%S")
        print("[*] Session Time:")
        print(f"Start Date: {self.session_time['start_date']}")
        print(f"Start Time: {self.session_time['start_time']}")
        print(f"End Date: {self.session_time['end_date']}")
        print(f"End Time: {self.session_time['end_time']}")
        print("[*] Session Duration:")
        start = datetime.strptime(f"{self.session_time['start_date']} {self.session_time['start_time']}",
                                  "%m-%d-%Y %H:%M:%S")
        end = datetime.strptime(f"{self.session_time['end_date']} {self.session_time['end_time']}", "%m-%d-%Y %H:%M:%S")
        duration = end - start
        print(f"Duration: {duration}")

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
            # check bluetooth system process
            print("[*] Checking Bluetooth...")

        except Exception as e:
            print(Fore.RED + f"[X] Error checking Bluetooth: {e}")

    def check_gps(self):
        try:
            print("[*] Checking GPS...")
            gpsd.connect()
            if gpsd.get_current() is None:
                self.gps = False
                print(Fore.RED + "[X] GPS: DOWN")
            else:
                self.gps = True
                print(Fore.GREEN + "[*] GPS: OK")
        except ConnectionError as ne:
            print(Fore.RED + f"[X] Error connecting to GPS: {ne}")
        except Exception as e:
            print(Fore.RED + f"[X] Error getting GPS status: {e}")

    def get_location(self):
        if not self.gps:
            print(Fore.RED + "[X] GPS is not enabled.")
            return
        try:
            # TODO: GET LOCATION FROM GPS
            print("[*] TODO: Getting Location...")
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
            headers = {"Authorization": f"Bearer {wigle_api_key}"}
            with httpx.post("https://api.wigle.net/api/v2/file/upload", headers=headers,
                            files={"file": open(file, "rb")}) as r:
                # https://api.wigle.net/csvFormat.html
                print(r.text)
        except Exception as e:
            print(Fore.RED + f"[X] Error uploading to WiGLE: {e}")

    def shutdown(self):
        self.end_time = datetime.now().strftime("%H:%M:%S")
        self.end_date = datetime.now().strftime("%m-%d-%Y")
        print(Fore.LIGHTRED_EX + "[!] Shutting down.")
        sys.exit(0)


def main():
    """Main function of Warwheel project"""

    # initialize colorama
    init(autoreset=True)

    warwheel = WarWheel()
    print(f"Start Date: {warwheel.start_date}")
    print(f"Start Time: {warwheel.start_time}")
    warwheel.shutdown()
    print(f"End Date: {warwheel.end_date}")
    print(f"End Time: {warwheel.end_time}")


if __name__ == '__main__':
    main()
