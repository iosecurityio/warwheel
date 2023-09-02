# TESTS
from colorama import init, Fore, Back, Style
from bleak import BleakScanner as bs

class WarWheel:

        def splash(self):
                print(Fore.BLUE + Style.DIM + """
M""MMM""MMM""M                   """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M""MMM""MMM""M dP                         dP""" + Fore.BLUE + Style.DIM + """ 
M  MMM  MMM  M                   """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  MMM  MMM  M 88                         88""" + Fore.BLUE + Style.DIM + """ 
M  MMP  MMP  M .d8888b. 88d888b. """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  MMP  MMP  M 88d888b. .d8888b. .d8888b. 88""" + Fore.BLUE + Style.DIM + """ 
M  MM'  MM' .M 88'  `88 88'  `88 """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  MM'  MM' .M 88'  `88 88ooood8 88ooood8 88""" + Fore.BLUE + Style.DIM + """
M  `' . '' .MM 88.  .88 88       """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M  `' . '' .MM 88    88 88.  ... 88.  ... 88""" + Fore.BLUE + Style.DIM + """
M    .d  .dMMM `88888P8 dP       """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """M    .d  .dMMM dP    dP `88888P' `88888P' dP""" + Fore.BLUE + Style.DIM + """
MMMMMMMMMMMMMM                   """ + Fore.LIGHTBLUE_EX + Style.BRIGHT + """MMMMMMMMMMMMMM""")


if __name__ == '__main__':
    init(autoreset=True) # initialize colorama
    WarWheel().splash()