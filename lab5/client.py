
import json
import random
import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $host:$port $dst_file <$input_file\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  host = sys.argv[1].split(':')[0]
  port = int(sys.argv[1].split(':')[1])
  dst_file = sys.argv[2]
except (IndexError, ValueError):
  usage()

def get_chunk(chunk_size=512, stream=sys.stdin):
  while True:
    data = stream.read(chunk_size) 
    if not data:
      break
    yield data

def compute_checksum(data, bound=256):
  return sum(data.encode()) % bound






def reliable_send(udp_socket, sequence, data, packet_size=1024):
  # initialize/create packet
  # serialize packet
  # loop:
  #   unreliably send packet using udp_socket
  #   wait for acknowledgment packet
  #   check acknowledgement packet's sequence number
  #     if it is the same as current sequence number, repeat the loop
  #     otherwise, exit the loop
  # return the acknowledgement packet's sequence number
  packet = dict()
  packet['data'] = data
  packet['sequence'] = sequence
  packet['checksum'] = compute_checksum(data)
  
  # check socket for incoming sequence number
  while True:
    udp_socket.send(json.dumps(packet).encode())
    print (udp_socket.recv(packet_size))
    incoming = json.loads(udp_socket.recv(packet_size)).decode('utf-8')
    if incoming['sequence'] == sequence:
      continue
    if incoming['sequence'] == sequence+1:
      break

  return incoming['sequence']
                  




def client(host, port, dst_file):
  sequence = 0
  termination_string = str(random.random())

  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udp_socket.bind(('localhost',int(port)))
  print("listening on port %d" % int(port))
  try:
    udp_socket.connect( (host, port) )
  except socket.gaierror:
    sys.stderr.write("Invalid Host: {}\n".format(host))
    exit(1)

  sequence = reliable_send(udp_socket, sequence, termination_string)
  sequence = reliable_send(udp_socket, sequence, dst_file)

  for chunk in get_chunk():
    sequence = reliable_send(udp_socket, sequence, chunk)

  sequence = reliable_send(udp_socket, sequence, termination_string)

  udp_socket.close()


if __name__ == "__main__":
  client(host, port, dst_file)


