import platform

if platform.system() == 'Linux':
	import models as models
	import scanport as scanport
else:
	from scanner import models as models
	from scanner import scanport as scanport

import ipaddress

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
						new_port.scan = new_scan
						new_port.save()
						port_num +=1
				else:
					new_port = models.Port()
					new_port.ip = new_ip
					new_port.number = port
					new_port.scan = new_scan
					new_port.save()

	run_scan(new_scan)

	return new_scan


def run_scan(scan):

	print(scan.name)

	ip_addresses = models.Ip.objects.filter(scan=scan)

	for ip in ip_addresses:
		ports = models.Port.objects.filter(ip=ip)
		print(ip.ip)

		for port in ports:
			scan_result = scanport.scan_port(ip.ip, port.number)
			port.active = scan_result
			port.save()




