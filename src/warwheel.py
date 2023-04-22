#Warwheel v0.0.1
#Created by: @113n
#https://github.com/iosecurityio/warwheel
#Portable War Driving Tool
# -*- coding: utf-8 -*-

from colorama import init, Fore
from datetime import datetime, timedelta
import httpx
import kismet_rest
init(autoreset=True) # initialize colarama

kismet_user = ""
kismet_pass = ""
wigle_api_key = ""

class warwheel:
        """Creates a warwheel object"""

        def __init__(self):
                self.start_time = ""
                self.start_date = datetime.now().strftime("%m-%d-%Y")
                self.start_location = ""
                self.internet = False
                self.bluetooth = False
                self.gps = False
                self.kismet = False
                self.splash()
                self.startup()


        def splash(self):
                print(Fore.LIGHTGREEN_EX + """
__        __        """ + Fore.GREEN + """          _               _ """ + Fore.LIGHTGREEN_EX + """
\ \      / /_ _ _ __""" + Fore.GREEN + """__      _| |__   ___  ___| |""" + Fore.LIGHTGREEN_EX + """
 \ \ /\ / / _` | '__""" + Fore.GREEN + """\ \ /\ / / '_ \ / _ \/ _ \ |""" + Fore.LIGHTGREEN_EX + """
  \ V  V / (_| | |  """ + Fore.GREEN + """ \ V  V /| | | |  __/  __/ |""" + Fore.LIGHTGREEN_EX + """
   \_/\_/ \__,_|_|  """ + Fore.GREEN + """  \_/\_/ |_| |_|\___|\___|_|""")
                print("warwheel.py v0.0.1")
                print("Created by: @113n")
                print("https://github.com/iosecurityio/warwheel")
                print("*" * 50)

        def start(self):
                self.start_time = datetime.now().strftime("%H:%M:%S")
                #self.start_location = input("Where are you starting from? ")

        def check_internet(self):
               print("Checking internet")

        def check_bluetooth(self):
               print("Checking Bluetooth")

        def check_gps(self):
               print("Checking GPS...")

        def check_kismet(self):
                print("Checking Kismet...")
                devices = kismet_rest.Devices()
                for device in devices.all(ts=1546300800):
                        print(device)

        def upload_scan(self, file):
                """Upload a scan to WiGLE.net via the API
                :param file: The file to upload

                Reference: https://api.wigle.net/swagger#/Network%20observation%20file%20upload%20and%20status./upload
                """

                try:
                        headers = {"Authorization": f"Bearer {wigle_api_key}"}
                        with httpx.post("https://api.wigle.net/api/v2/file/upload", headers=headers,files={"file": open(file, "rb")}) as r:
                                print(r.text)
                except Exception as e:
                        print(f"[X] Error uploading to WiGLE: {e}")

        def startup(self):
                self.check_internet()
                self.check_bluetooth()
                self.check_gps()
                self.start()

def main():
      print("Starting warwheel...")
      warwheeler = warwheel()
      print(warwheeler.start_date)

if __name__ == '__main__':
    main()