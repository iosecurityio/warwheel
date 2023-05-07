#Warwheel v0.0.1b
#Created by: Allen Montgomery <allen@iosecurity.io>
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
kismet_api_key = ""

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
                print("-" * 48)

        def start(self):
                self.start_time = datetime.now().strftime("%H:%M:%S")
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
                        headers = {"Authorization": f"Bearer {wigle_api_key}"}
                        with httpx.post("https://api.wigle.net/api/v2/file/upload", headers=headers,files={"file": open(file, "rb")}) as r:
                                print(r.text)
                except Exception as e:
                        print(Fore.RED + f"[X] Error uploading to WiGLE: {e}")

        def shutdown(self):
                self.end_time = datetime.now().strftime("%H:%M:%S")
                self.end_date = datetime.now().strftime("%m-%d-%Y")
                print(Fore.LIGHTRED_EX + "[!] Shutting down.")



def main():
        """Main function of Warwheel project"""
        
        warwheeler = warwheel()
        print(f"Start Date: {warwheeler.start_date}")
        print(f"Start Time: {warwheeler.start_time}")
        warwheeler.shutdown()
        print(f"End Date: {warwheeler.end_date}")
        print(f"End Time: {warwheeler.end_time}")

if __name__ == '__main__':
    main()
