#!/usr/bin/python3
# URL fuzzer written for Offsec Proving Grounds machine "RussianDolls"
# NOTE: The server first appears to be vulnerable to RFI but I couldn't seem to
# take advantage of that. Because of the way the url is accessing local resources
# I decided to scan for ports only open on the local machine to see if we could
# take advantage that way. Doing all 65535 port is pretty slow but you can just 
# change loop iteration if you would like. 
#
# Written by Rob Flemen
# Author Github: https://github.com/rflemen
# Author YouTube: https://www.youtube.com/@RobFlemen 
# 12/31/2025

import requests
import argparse
import time

# Setup arguments and parser
parser = argparse.ArgumentParser(description="A script that fuzzes a URL for response code 200 for SSRF.")
parser.add_argument("--url", required=True, help="Target url")
args = parser.parse_args()


### PRINT BANNER ###        
print("SCRiPT By:                ")
print("        ,------.           ")            
print(",--,--, |  .--. ',--,--,--.") 
print("|      ;|  '--' ||        |") 
print("|  ||  ||  | --' |  |  |  |") 
print("`--''--'`--'     `--`--`--'")                            
print("URL Fuzzer for SSRF")
print("Written for Offsec PG machine - RussianDolls") 
time.sleep(2)


### BEGIN SCAN ###
base_url = args.url
open = 0

for port in range (8100):
    target_url = base_url + ":" + str(port)
    response = requests.get(target_url, timeout=3)
    if response.status_code != 500:
        open =+ open + 1
        print(f"[\033[92m\N{CHECK MARK}\033[00m] Port: {port} >>> Status code = [\033[92m{response.status_code}\033[00m]")
    	
print(f"Scan done, it appears there are {open} port(s) open!")
