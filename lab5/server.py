
import json
import sys
import socket

def usage():
  usg_str = "Usage: python3 $port\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  port = int(sys.argv[1])
except (IndexError, ValueError):
  usage()

def compute_checksum(data, bound=256):
  return sum(data.encode()) % bound




def reliable_recv(udp_socket, packet_size=1024):
  while True:
    packet = json.loads(udp_socket.recv(packet_size)).decode()
    print(packet['checksum']);
    print(compute_checksum(packet["data"]))

    # if the packet's check sum is equal
    # to the computed checksum of recieved data
    # then send back the next sequence number as a confirmation
    if packet['checksum'] == compute_checksum(packet['data']):
      udp_socket.send((packet['sequence']+1))
    else:       
      #initial sqnc number is the packets sequence number
      udp_socket.send(packet['sequence']);
    continue;
  return packet;
  # initialize/create acknowledgement packet
  # loop:
  #   receive packet from client
  #   deserialize packet
  #   compute checksum of data in packet
  #   compare computed checksum with checksum in packet
  #   if they match:
  #     set acknowledgement packet sequence to packet's sequence + 1
  #     send acknowledgement packet to client
  #   else:
  #     set acknowledgement packet sequence to packet's sequence
  #     send acknowledgement packet to client
  #     repeat loop
  # return packet's data



def server(port):
  udp_socket = socket.socket(socket.SOCK_DGRAM)
  print('Server constructor initialized')
  host = '127.0.0.1'
  udp_socket.bind((host, port))
  udp_socket.listen()
  print('Listening on port ' + str(port))
  conn = udp_socket.accept()[0]
  print('Connection accepted\n')
 
  # first recieve termination string
  # then recieve dst_file;
  term_string = reliable_recv(udp_socket)
  dst_file = reliable_recv(udp_socket)


  
  with open(dst_file, "w") as stream:
    while True:
      data = reliable_recv(udp_socket)
      if (data == term_string or data == 'quit'):
        break
      stream.write(data)
  udp_socket.close()




if __name__ == "__main__":
  server(port)





