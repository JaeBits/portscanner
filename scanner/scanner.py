import platform

if platform.system() == 'Linux':
	import models
else:
	from scanner import models
	
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
						new_port.save()
						port_num +=1
				else:
					new_port = models.Port()
					new_port.ip = new_ip
					new_port.number = port
					new_port.save()





	return ('hi')

def run_scan():
	print('run')
	return('run')