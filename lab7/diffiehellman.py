

import sys
import random
import math

# do not modify this function
def get_input():
  # default prime and base
  prime = 64303
  base = 6

  # attempt to get input
  try:
    a_pk = int(sys.argv[1])
    b_pk = int(sys.argv[2])
    if len(sys.argv) > 3:
      prime = int(sys.argv[3])
      base = int(sys.argv[4])
  except (IndexError, ValueError):
    fmt_str = "Usage:\n" \
              "\tpython3 {} <a_pk> <b_pk> [<prime> <base>]\n"
    sys.stderr.write(fmt_str.format(sys.argv[0]))
    sys.exit(1)

  # return input
  return a_pk, b_pk, prime, base



# push send1 a to b
# push send2 b to a
# use mutually sent data to calculate a pub key
if __name__ == "__main__":
  a_pk, b_pk, prime, base = get_input()
  sys.stdout.write("Using (prime,base) = (" + str(prime) + ","+str(base)+")\n")
  send1 = int(math.pow(base,a_pk) % prime)
  send2 = int(math.pow(base,b_pk) % prime)
  pub = int(math.pow(send1,b_pk) % prime)
  pub2 = int(math.pow(send2,a_pk) %prime)


  sys.stdout.write("Public keyA: "+str(send1) + "\nPublic keyB: " + str(send2) + "\n")
  sys.stdout.write("A calculates: "+str(pub) + "\nB calculates: " + str(pub2) + "\n")
  sys.exit(1)




