#!/usr/bin/python

import sys
from scanner import scanport as scanport
import ipaddress

def validate_port(port):
	if port.isdigit():
		return int(port)
	else:
		print('Not a valid port: ' + port)
		return -1
		
def run_scan(port, ip_result):
	if port != -1:
		if ip_result != -1:
			response = scanport.scan_port(ip_result, port)
			if response == 1:
				print('Port is open!')
			elif response == 0:
				print('Port is closed')
			else:
				print('Port is filtered')


if sys.argv[1] == '-ip':
	if sys.argv[3] == '-p':

		port = validate_port(sys.argv[4])
		ip_result = sys.argv[2]

		run_scan(port, ip_result)


elif sys.argv[1] == '-p':
	if sys.argv[3] == '-ip':

		port = validate_port(sys.argv[2])
		ip_result = sys.argv[4]

		run_scan(port, ip_result)


else:
	print('Welcome to the command line version of the port scanner')
	print('Commands:')
	print('-ip <Ip Address>: to specify ip address')
	print('-p <port number>: to specify port number\n')
	print('use python manage.py runserver to start web application version (requires sqlite db)')


