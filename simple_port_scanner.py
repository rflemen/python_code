# A simple multithreaded port scanner written by Rob Flemen
import pyfiglet
import re
 
banner = pyfiglet.figlet_format("Simple Port Scanner")
print(banner)
print("\t\t\t by Rob Flemen\n")

# This will be an argument at some point
filename = 'Text_files\ip_addresses.txt'

# Read from a file (this will be for reading IP addresses to scan)
try:
    with open(filename) as file_object:
        ips = file_object.readlines()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# Determion if IP addresses in file are valid
# REGEX pattern taken from "https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html"
pattern = re.compile('''(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$)''')
valid =[] 
invalid=[] 

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
print("Valid IPs") 
print(valid)

print("Invalid IPs") 
print(invalid) 







