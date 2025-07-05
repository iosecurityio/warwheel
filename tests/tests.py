#!python3
# This file is used to test the warwheel module
from datetime import datetime

from colorama import init

# Turn on colors
init(autoreset=True)


class Warwheel:
    """Creates a Warwheel object"""

    def __init__(self):
        self._start_time = ""
        self._start_date = ""
        self._splash()
        self._start()

    def _get_start_time(self):
        return self._start_time

    def _set_start_time(self, time):
        self._start_time = time

    def _get_start_date(self):
        return self._start_date

    def _set_start_date(self, date):
        self._start_date = date

    def _splash(self):
        """Splash screen for warwheel tests"""
        print("Warwheel Tests")
        link = "https://github.com/iosecurityio/warwheel"
        sep = "*" * len(link)
        print(link)
        print(sep)

    def _start(self):
        """Start the tests"""
        now = datetime.now()
        # Set the startup time and date
        self._set_start_time(now.strftime("%H:%M:%S"))
        self._set_start_date(now.strftime("%m-%d-%Y"))
        print(f"Start Time: {self._get_start_time()}")
        print(f"Start Date: {self._get_start_date()}")

        print("Hello World!")


def main():
    """Runs warwheel tests"""

    # Create a warwheel object
    warwheel = Warwheel()


if __name__ == '__main__':
    main()
