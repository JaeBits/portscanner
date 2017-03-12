# this is the scan class that performs the scan. It is shared by the command line and web app

from scapy.all import *
import ipaddress


def scan_port(ip_address, dst_port):

	src_port = RandShort()
	
	scan = sr1(IP(dst=ip_address)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
	
	if scan is None:
		return 0
	elif(scan.haslayer(TCP)):
		if(scan.getlayer(TCP).flags==0x12):
			return 1
	
	return 2