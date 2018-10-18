import sys
import socket

def usage():
  usg_str = "Usage: python3 {} $host:$port\n"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

try:
  host = sys.argv[1].split(':')[0]
  port = int(sys.argv[1].split(':')[1])
except (IndexError, ValueError):
  usage()

def get_message(stream=sys.stdin):
  try:
    for line in stream:
      yield line.strip()
  except KeyboardInterrupt:
    return





def encrypt(plaintext, key):
  # pretend this function is already implemented
  return plaintext




def secure_send(udp_socket, message):
  key = date.datetime.utcnow() % 32
  # save this number locally, and then encrypt with your key
  # call the diffiehellman function and send udp_socket base^(a_pk) % prime
  # message = encrypt(message,key)
  message = encrypt(message,key)
  return udp_socket.send(message.encode())





def talk(host, port):
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
  term_string = "quit"
  
  try:
    udp_socket.connect( (host, port) )
  except socket.gaierror:
    sys.stderr.write("Invalid Host: {}\n".format(host))
    exit(1)

  for message in get_message():
    secure_send(udp_socket, message)
    if message == term_string:
      break

  udp_socket.close()


if __name__ == "__main__":
  talk(host, port)





