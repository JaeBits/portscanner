from scanner import models

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from scanner import scanner as scanner
import ipaddress

def index(request):      


	return render(request, 'index.html')


def scans(request):
	scans = models.Scan.objects.all()

	return render(request, 'scans.html', {'scans':scans})



def new_scan(request):

	if request.method == 'POST':
		# create a form CodeForm and populate it with data from the request:
		form_scan = ScanForm(request.POST)
		# check whether it's valid:
		if form_scan.is_valid():
			
			# begin parse
			name = form_scan.cleaned_data['name']
			ip_addresses = form_scan.cleaned_data.get('ip_addresses')
			ports = form_scan.cleaned_data['ports']
			
			for port in ports:
				print(port)

			new_scan = scanner.save_scan(name, ip_addresses, ports)
			
			print(new_scan.id)
			# redirect to a new URL:
			url = '/scan/' + str(new_scan.id)
			return HttpResponseRedirect(url)

	else:
		form_scan = ScanForm()

	return render(request, 'scan.html', {'form_scan':form_scan})

def rescan(request, id):
	scan = models.Scan.objects.get(id=id)
	scanner.run_scan(scan)
	url = '/scan/' + str(scan.id)
	return HttpResponseRedirect(url)



def scan(request, id):

	scan = models.Scan.objects.get(id=id)
	ip_addresses = models.Ip.objects.filter(scan=scan)
	ports = models.Port.objects.filter(scan=scan)

	return render(request, 'results.html', {'scan':scan, 'ip_addresses':ip_addresses, 'ports':ports})


class ScanForm(forms.Form):
	name = forms.CharField(required=True, label="", help_text="",widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Name for this scan' }))
	ip_addresses = forms.CharField(required=False, label="", help_text="",widget=forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Please input an ip address, ip addresses seperated by commas, or an ip address network. ex: 192.168.208.101, 192.168.207.0/24' }))
	ports = forms.CharField(required=False, label="", help_text="",widget=forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Please input ports to be scanned seperated by commas or a range with a dash. ex: 21-25, 53, 80, 445-447' }))
	
	def remove_whitespaces(self, code):
		code = code.strip()
		code = code.replace(" ", "")
		code = ''.join(code.split())
		return code

	def clean_ip_addresses(self):
		'''Ensures valid ip addresses'''
		ips = self.cleaned_data.get('ip_addresses')
		ips = self.remove_whitespaces(ips)

		ips = ips.split(",")

		for ip in ips:
			try:
				network = ipaddress.IPv4Network(ip)
			except ValueError:
				raise forms.ValidationError('Ip Addresses must be in the following format: xxx.xxx.xxx.xxx seperated by commas or with a valid network range. Please check syntax near ip address ' + ip)
		
		return ips

	def clean_ports(self):
		'''Ensures valid ports'''
		ports = self.cleaned_data.get('ports')
		ports = self.remove_whitespaces(ports)
		
		#split on comma
		ports = ports.split(",")

		#check each port is valid
		for port in ports:

			#check if port is range
			port_range = port.split("-")

			if len(port_range) > 1:
				if port_range[0] > port_range [1]:
					raise forms.ValidationError('Not a valid port range. Please check syntax near port ' + port_range[0])


			for range_port in port_range:
				if range_port.isdigit():
					pass
				else:
					raise forms.ValidationError('Ports must be integer values seperated by commas or a range with a dash. Please check syntax near port ' + range_port)


		return ports
