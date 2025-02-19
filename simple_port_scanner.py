# A simple single threaded port scanner written by Rob Flemen
import pyfiglet
import re
import argparse
import socket


# Function to check if a port is open on an IP address
def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False


banner = pyfiglet.figlet_format("Port Scanner")
print("\nA SIMPLE...")
print(banner)
print("\t\t\t\t\t\t by Rob Flemen\n")


#Take filename as argument
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the file to be read")
parser.add_argument("-p", "--port", help="the port to be scanned", type=int)
parser.add_argument("-n", "--name", help="the name of the person running the program")
args = parser.parse_args()
print(f"The filename read in is: {args.filename}")
print(f"The port to be scanned is: {args.port}\n")


# Argument (file name) fed to variable
filename = args.filename
username = args.name
port = args.port


# Read from a file (this will be for reading IP addresses to scan)
try:
    with open(filename) as file_object:
        ips = file_object.readlines()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


# Determion if IP addresses in file are valid IP addresses:
# REGEX pattern taken from "https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html 
# I did have to add an escape character "\" before the "\." for it to work completely correctly
pattern = re.compile('''(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$)''')
valid =[] 
invalid=[] 


#Add valid IP Addresses to the valid list and invalid IP addresses to the invalid list
for ip in ips: 
    ip = ip.rstrip() 
    result = pattern.search(ip) 
    # valid IP addresses 
    if result: 
      valid.append(ip) 
    # invalid IP addresses   
    else: 
      invalid.append(ip)


# Displaying the IP addresses (just for debugging) 
print(f"{args.name}, your list contains these valid IPs and they will be scanned") 
print(valid)
print(f"\n{args.name}, your list contains these invalid IPs and they will not be scanned") 
print(invalid) 


# Port scan valid IP addresses
print(f"\nScanning port {port} on the following IP addresses...")
for ip in valid: 
    if isOpen(ip, port): 
        print(f"[+]\tPort {port} is OPEN on {ip}") 
    else: 
        print(f"[-]\tPort {port} is CLOSED on {ip}")







