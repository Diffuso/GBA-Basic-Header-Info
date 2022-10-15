# GBA Basic Header Info
version = 0.1

import re
import sys
import os.path
from colorama import Fore, init
from data import region, publishers
init(autoreset=True)


# Check if there are passed arguments
if len(sys.argv) <= 1:
    print(Fore.YELLOW + f"[!] Usage: {sys.argv[0]} <filename>.gba")
else:
    # Check the filename extension
    if not ((sys.argv[1][-3:]).lower() == 'gba'):
        print(Fore.LIGHTRED_EX + "[X] Error. Extension must be .gba")
    else:
        filename = sys.argv[1]
        # Check if the file exists
        if not os.path.exists(filename):
            print(Fore.LIGHTRED_EX + f"[X] Error. File {filename} doesn't exist.")
        else:
            print(Fore.LIGHTGREEN_EX +"Opening ROM...")
            # Open the file
            with open(filename, 'rb') as rom:
                    rom_content = rom.read()
                    rom.close()
            # Get the basic info
            rom_header = re.findall(b"\xd4\xf8\x07(.*?)\x96", rom_content)
            # Check if there is info on the header
            # if not, print error message
            if len(rom_header) <= 0:
                print(Fore.LIGHTRED_EX + "[X] Error. ROM not licensed.")
            else:
               # Get internal name
                internal_name = rom_header[0].decode()[:-6]
                # Get rom region (E = USA, P = EUR, J = JPN...)
                rom_region = rom_header[0].decode()[-6:-2][-1]
                # Make the serial 
                serial = 'AGB-' + rom_header[0].decode()[-6:-2] + '-' + region[rom_region]
                # Publisher 
                publisher = rom_header[0].decode()[-2:]
                # Print ROM header info
                print(f"Internal name: {internal_name}")
                print(f"Region: {region[rom_region]}")
                print(f"Serial: {serial}")
                # Check if the publisher is defined or not
                if publisher in publishers:
                    print(f"Publisher ID: {publisher} ({publishers[publisher]})")
                else:
                    print(f"Publisher ID: {publisher} (Unknown)")