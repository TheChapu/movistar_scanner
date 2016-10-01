#!/usr/bin/evn python

from socket import *

def scan_port(ip, port,timeout=None):
	target = ip
	
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(timeout)
	result = sock.connect_ex((target,port))

	if(result == 0):
		return True
	else:
		return False

	sock.close()
