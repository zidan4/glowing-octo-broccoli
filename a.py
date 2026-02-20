from scapy.all import *
import os
import sys
import threading
import signal

interface = "en1"
target_ip = "172.16.1.71"
gateway_ip = "172.16.1.254"
packet_count = 1000

# set our interface
conf.iface = interface
# turn off output
conf.verb = 0
print "[*] Setting up %s" % interface
