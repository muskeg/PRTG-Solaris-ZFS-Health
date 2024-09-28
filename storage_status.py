#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PRTG Advanced SSH Sensor Script
This polls the server and ZFS pools for stats and health status
"""

import os

# Convert the human readable to bytes so we don't deal with units
units = {"B": 1, "K": 10**3, "M": 10**6, "G": 10**9, "T": 10**12}

def parseSize(size):
    number = size[:-1]
    unit = size[-1:]
    return int(float(number)*units[unit])



pools_list = []

zpool_list = os.popen("zpool list -Ho name,size,alloc,free,cap,health").read()

for pool_info in zpool_list.split("\n"):
    if pool_info:
        value = pool_info.split("\t")
        pools_list.append({ 'name': value[0], 'rawsize': value[1], 'allocated': value[2], 'free': value[3], 'used': value[4], 'health': value[5] })

status_text = "All pools healthy"

print("<prtg>")

for pool in pools_list:
    print("<result>")
    print("<channel>Utilisation " + pool.get("name") + "</channel>")
    print("<value>" + pool.get("used")[:-1] + "</value>")
    print("<unit>percent</unit>")
    print("<limitmaxwarning>80</limitmaxwarning>")
    print("<limitmaxerror>90</limitmaxerror>")
    print("</result>")
    print("<result>")
    print("<channel>Health " + pool.get("name") + "</channel>")
    print( "<customunit></customunit>")
    if pool.get("health") != "ONLINE":
         print("<warning>1</warning>")
         print("<value>1</value>")
         status_text = pool.get("name") + " : " + pool.get("health")
    else:
         print("<value>0</value>")
    print("<unit>custom</unit>")
    print("</result>")

"""
    print pool.get("name")
    print parseSize(pool.get("rawsize"))
    print parseSize(pool.get("allocated"))
    print parseSize(pool.get("free"))
    print pool.get("used")[:-1]
    if pool.get("health") != "ONLINE":
        print "<warning>1</warning>"
"""
print("<text>" + status_text + "</text>")
print("</prtg>")
