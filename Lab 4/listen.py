#! python3
# listen.py
# Listens on address and port and prints host messages

import socket
import sys
__author__ = 'Aaron Goldsmith'    

hosts = []
def listen(port):
    """ Listens on a port for incoming user/messages """
    MAX_BYTES = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind localhost to port
    sock.bind(('localhost',int(port)))
    print("listening on port %d" % int(port))
    while True:
        data, addr = sock.recvfrom(MAX_BYTES)
        data = data.decode('ascii','ignore')
        clientAddr = str(addr[0])
        if clientAddr not in hosts:
            hosts.append(clientAddr)

        # neccesary to check termination
        # before printing message 
        
        # termination condition
        if data[3:7].lower() == "quit":
            print(clientAddr + " has left the session")     
            if len(hosts) == 0: break
            continue

        # message from host
        if data[:3] == "{0}":
            print(clientAddr +":  "+data[3:])
    
    # close connection
    sock.close();


if len(sys.argv) == 2:
    listen(sys.argv[1])
else:
    print('Incorrect Usage.\nUsage: python3 %s $port' % sys.argv[0])

