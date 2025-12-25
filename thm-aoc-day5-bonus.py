# Use this to generate UUIDs for Advent of Cyber 2025 Day 5 Bonus Question #2
# Written by Rob Flemen with assistance from ChatGPT
# December 18th, 2025

import uuid
import datetime
import random
import re

UUID_EPOCH_START = datetime.datetime(1582, 10, 15, tzinfo=datetime.timezone.utc)

def mac_to_int(mac):
    """
    Convert MAC address string to 48-bit integer.
    """
    mac = mac.lower().replace("-", "").replace(":", "")
    if not re.fullmatch(r"[0-9a-f]{12}", mac):
        raise ValueError(f"Invalid MAC address: {mac}")
    return int(mac, 16)


def uuid1_from_datetime(dt, mac_address=None, clock_seq=None):
    """
    Generate a UUIDv1 from a specific UTC datetime and optional MAC address.
    """

    if dt.tzinfo is None:
        raise ValueError("Datetime must be timezone-aware")

    delta = dt - UUID_EPOCH_START
    timestamp = int(delta.total_seconds() * 10_000_000)

    if mac_address is not None:
        node = mac_to_int(mac_address)
    else:
        node = random.getrandbits(48)

    if clock_seq is None:
        clock_seq = random.getrandbits(14)

    time_low = timestamp & 0xFFFFFFFF
    time_mid = (timestamp >> 32) & 0xFFFF
    time_hi_version = ((timestamp >> 48) & 0x0FFF) | (1 << 12)

    clock_seq_low = clock_seq & 0xFF
    clock_seq_hi_variant = ((clock_seq >> 8) & 0x3F) | 0x80

    return uuid.UUID(fields=(
        time_low,
        time_mid,
        time_hi_version,
        clock_seq_hi_variant,
        clock_seq_low,
        node
    ))


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":

    MAC = "02:6c:cd:f7:d7:69" #Fake MAC address of THM machine

    for hour in range(20, 24):
        for minute in range(60):
            dt = datetime.datetime(
                2025, 11, 20,
                hour, minute, 0,
                tzinfo=datetime.timezone.utc
            )

            u = uuid1_from_datetime(
                dt,
                mac_address=MAC,
                clock_seq=0x2C99 #Fake randomness (seed) from THM machine
            )

            print(f"{u}")
