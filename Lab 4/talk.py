#! python3
# talk.py
# Sends messages to a server

import socket
import sys
__author__ = 'Aaron Goldsmith'    

def talk(host, port):
    # Try connecting to server at host, port
    try:
        addr_info = socket.getaddrinfo(host,port)
    # Print exception if error exists, then exits
    except socket.gaierror:
        print(socket.gai_strerror())
        exit()

    # initialize a socket connection, and then connect

    conn = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # this is where our ip address is
    conn.connect( (addr_info[0][4]) )

    # Generic header
    header = '{0}'
    while True:
        # prompting user to type message
        msg = header + input("Type Message: ")
        # replace new lines with empty string
        msg = msg.replace("\n", "")
        #encode string into ascii and ignores special chars
        conn.send(msg.encode('ascii','ignore'))

        # breaks loop if host types `quit`
        if msg[3:7].lower() == "quit":
            break

    # close connection outside loop
    conn.close()


if len(sys.argv) == 3:
    talk(sys.argv[1],sys.argv[2])
else:
    print('Incorrect Usage.\nUsage: python3 %d $port' % sys.argv[0])
