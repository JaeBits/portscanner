import platform

if platform.system() == 'Linux':
	import models
else:
	from scanner import models

import ipaddress
from scapy.all import *

def save_scan(name, ip_addresses, ports):

	new_scan = models.Scan()
	new_scan.name = name
	new_scan.save()

	for ip in ip_addresses:
		network = ipaddress.IPv4Network(ip)
		for ip in network:
			new_ip = models.Ip()
			new_ip.ip = str(ip)
			new_ip.scan = new_scan
			new_ip.save()

			for port in ports:
				
				port_range = port.split("-")
				
				if len(port_range) > 1:
					port_num = int(port_range[0])
					port_max = int(port_range[1])
					while port_num <= port_max:
						new_port = models.Port()
						new_port.ip = new_ip
						new_port.number = port_num
						new_port.save()
						port_num +=1
				else:
					new_port = models.Port()
					new_port.ip = new_ip
					new_port.number = port
					new_port.save()

	return new_scan

def run_scan(scan):

	ip_address = models.Ip.objects.filter(scan=scan)

	for ip in ipaddress:
		ports = models.Port.objects.filter(ip=ip)

		for port in ports:
			src_port = RandShort()
			dst_port = port.number
			i = ip.ip

			scan = sr1(IP(dst=i)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
			
			if scan is None:
				port.active = 0
			elif(scan.haslayer(TCP)):
				if(scan.getlayer(TCP).flags==0x12):
					port.active = 1
			else:
				port.active = 2

			port.save()

	

	return('run')
