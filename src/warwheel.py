# Warwheel v0.0.1b
# Created by: Allen Montgomery <allen@iosecurity.io>
# https://github.com/iosecurityio/warwheel
# Portable War Driving Tool
# -*- coding: utf-8 -*-

from colorama import init, Fore
from datetime import datetime, timedelta
import httpx
import kismet_rest
from pathlib import Path
import os
from dotenv import load_dotenv


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
        print(
            Fore.LIGHTGREEN_EX
            + """
__        __        """
            + Fore.GREEN
            + """          _               _ """
            + Fore.LIGHTGREEN_EX
            + """
\ \      / /_ _ _ __"""
            + Fore.GREEN
            + """__      _| |__   ___  ___| |"""
            + Fore.LIGHTGREEN_EX
            + """
 \ \ /\ / / _` | '__"""
            + Fore.GREEN
            + """\ \ /\ / / '_ \ / _ \/ _ \ |"""
            + Fore.LIGHTGREEN_EX
            + """
  \ V  V / (_| | |  """
            + Fore.GREEN
            + """ \ V  V /| | | |  __/  __/ |"""
            + Fore.LIGHTGREEN_EX
            + """
   \_/\_/ \__,_|_|  """
            + Fore.GREEN
            + """  \_/\_/ |_| |_|\___|\___|_|"""
        )
        print("Name: warwheel.py v0.0.2b")
        print("Author: allen@iosecurity.io")
        print("Source: https://github.com/iosecurityio/warwheel.git")
        print("-" * 48)

    def start(self):
        """Start Warwheel"""

        print(Fore.LIGHTGREEN_EX + "[*] Starting Warwheel...")
        self.start_time = datetime.now().strftime("%H:%M:%S")
        print(f"Start Date: {self.start_date}")
        print(f"Start Time: {self.start_time}")
        self.check_internet()
        self.check_bluetooth()
        self.check_gps()
        self.get_location()
        # TODO: Get start location from GPS
        self.start_location = "get location from gps"

    def check_internet(self):
        """Check Internet Connection"""

        try:
            print("[*] Checking Internet Connection...")
            with httpx.Client() as client:
                r = client.get("https://ipinfo.io")
                if r.status_code == 200:
                    self.internet = True
                    print(Fore.GREEN + "[*] Internet Connection: OK")
                else:
                    self.internet = False
                    print(Fore.RED + "[X] Internet Connection: DOWN")
        except Exception as e:
            print(f"[X] Error checking Internet Connection: {e}")

    def check_bluetooth(self):
        """Check Bluetooth Service"""

        try:
            print("[*] Checking Bluetooth...")
            # TODO: Check bluetooth status
        except Exception as e:
            print(Fore.RED + f"[X] Error checking Bluetooth: {e}")

    def check_gps(self):
        """Check GPS Service"""

        try:
            print("[*] Checking GPS...")
            # TODO: Check GPS Status
        except Exception as e:
            print(Fore.RED + f"[X] Error checking GPS: {e}")

    def get_location(self):
        """Get location from GPS"""

        if not self.gps:
            print(Fore.RED + "[X] GPS is not enabled.")
            return
        try:
            print("[*] Getting Location...")
            # TODO: Get location from GPS
        except Exception as e:
            print(Fore.RED + f"[X] Error getting Location: {e}")

    def check_kismet(self):
        """Check Kismet Service"""

        try:
            print("[*] Checking Kismet...")
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

        wigle_api_key = os.getenv("WIGLE_API_KEY")

        try:
            headers = {"Authorization": f"Bearer {wigle_api_key}"}
            with httpx.post(
                "https://api.wigle.net/api/v2/file/upload",
                headers=headers,
                files={"file": open(file, "rb")},
            ) as r:
                print(r.text)
        except Exception as e:
            print(Fore.RED + f"[X] Error uploading to WiGLE: {e}")

    def shutdown(self):
        """Shutdown Warwheel"""

        # TODO: Shutdown all services
        print("Shutting down...")
        self.end_time = datetime.now().strftime("%H:%M:%S")
        print(f"End Time: {self.end_time}")
        self.end_date = datetime.now().strftime("%m-%d-%Y")
        print(f"End Date: {self.end_date}")
        print(Fore.LIGHTRED_EX + "[!] Shutting down.")


def main():
    """Main function of Warwheel project"""

    # initialize colarama
    init(autoreset=True)

    # Load environment variables
    try:
        env_path = Path(".") / ".env"
        load_dotenv(dotenv_path=env_path)
    except Exception as e:
        print(f"Error loading environment variables: {e}")

    ww = warwheel()
    ww.shutdown()


if __name__ == "__main__":
    main()
