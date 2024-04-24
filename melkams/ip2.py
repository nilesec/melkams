#!/usr/bin
import requests
from ip2geotools.databases.noncommercial import DbIpCity
import os
import subprocess
os.system(
     f" sudo chmod +x banner && sudo ./banner"
 )

def get_info_from_ip(ip_address):
    """Gets information about an IP address."""
    res = DbIpCity.get(ip_address)
    info = {
        "ip_address": ip_address,
        "city": res.city,
        "region": res.region,
        "country": res.country,
        "latitude": res.latitude,
        "longitude": res.longitude,
    }
    return info

if __name__ == "__main__":
    ip_address = input("Enter IP address: ")
    info = get_info_from_ip(ip_address)
    print(info)
