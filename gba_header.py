# GBA Basic Header Info
version = 0.2

import re
import sys
import os.path
from colorama import Fore, init
from data import region, publishers
init(autoreset=True)


# Check if there are passed arguments
if len(sys.argv) <= 1:
    print(Fore.YELLOW + f"[!] Usage: {sys.argv[0]} <filename1>.gba <filename2>.gba <filename3>.gba")
else:
    if len(sys.argv) > 1:
        for rom in range(1, len(sys.argv)):
            # Check the filename extension
            if not ((sys.argv[rom][-3:]).lower() == 'gba'):
                print(Fore.LIGHTRED_EX + f"[X] Error ({sys.argv[rom]}). Extension must be .gba")
            else:
                filename = sys.argv[rom]
                # Check if the file exists
                if not os.path.exists(filename):
                    print(Fore.LIGHTRED_EX + f"[X] Error. File '{filename}' doesn't exist.")
                else:
                    print(Fore.LIGHTGREEN_EX + f"[>] Opening ROM {sys.argv[rom]}...")
                    # Open the file
                    with open(filename, 'rb') as rom_:
                            rom_content = rom_.read()
                            rom_.close()
                    # Get the basic info
                    rom_header = re.findall(b"\xd4\xf8\x07(.*?)\x96", rom_content)
                    # Check if there is info on the header
                    # if not, print error message
                    if len(rom_header) <= 0:
                        print(Fore.LIGHTRED_EX + f"[X] Error. ROM {sys.argv[rom]} not licensed.")
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
