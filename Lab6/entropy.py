import sys
import generate
import math

def usage():
  usg_str = "Usage: python3 entropy.py"
  sys.stderr.write(usg_str.format(sys.argv[0]))
  exit(1)

def fitness(count, total):
  if(total!=0):
    num = float(count/total)
    return (num * math.log2(num))
  return 0  



try:
  entrop = 0
  Count = 1
  # initialize an array of size 256 of all 0's
  valCount = [0 for i in range(257)];
  for char in sys.stdin.read():
    if char == '##END##':
      sys.stdout.write(str(entrop))
      break
    valCount[ord(char)] += 1
    iterations = valCount[ord(char)]
    entrop -= fitness(iterations,Count)
    Count += 1
  sys.stdout.write(str(entrop)+"\n")
  
except (IndexError, ValueError):
    usage()

