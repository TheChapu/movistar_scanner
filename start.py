#!/usr/bin/evn python

from port_scanner import scan_port
from parser_html import get_router_data

segmento_segundo_par = '190.162.'

# Iterar segundo par
for i in range(1,255):
	segmento_tercer_par = segmento_segundo_par + str(i) + '.'
	cantidad_vulnerables = 0
	
	#Avisar inicio segmento
	print 'Scanning ' + segmento_tercer_par + '0/24'
	
	for i in range(1,255):
		#Armar IP
		ip_to_scan = segmento_tercer_par + str(i+1)
	
		# Scan
		print "Target: {0}".format(ip_to_scan)
		result = scan_port(ip_to_scan, 80, timeout=0.3)
		
		# Router vulnerable
		# Obtener datos Wifi
		if(result):
			#get_router_data(ip_to_scan)
			print '> '+ip_to_scan+' puerto 8000 abierto... informacion registrada!'
			cantidad_vulnerables += 1
			
	print "Segmento " + segmento_tercer_par + '0/24 finalizado. Vulnerables: ' + str(cantidad_vulnerables)
		

