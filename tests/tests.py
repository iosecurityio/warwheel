# TESTS
from colorama import init, Fore
from datetime import datetime, timedelta
import httpx
init(autoreset=True) # initialize colorama


class warwheel:
        """Creates a warwheel object"""

        def __init__(self):
                self.start_time = ""
                self.start_date = datetime.now().strftime("%m-%d-%Y")
                self.start_location = ""
                self.splash()

        def splash(self):
                print
                print("Warwheel v0.0.1")
                print("Created by: @113n")
                print("https://github.com/iosecurityio/warwheel")
                print("*" * 50)

        def start(self):
                self.start_time = datetime.now().strftime("%H:%M:%S")
                #self.start_location = input("Where are you starting from? ")

def main():
      print("Testing warwheel...")
      warwheeler = warwheel()
      print(warwheeler.start_date)

       
if __name__ == '__main__':
    main()