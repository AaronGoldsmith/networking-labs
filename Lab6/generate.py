import random
import math
import sys

##  To begin, every character will have an equal 'score' 
##       i can create an array of 256 integers and each time
##       I come across a character, I increase the value at 
##      position arr[int(chr)
  
def random_data(size):
  """ Generates random ascii chars of length size bytes
      by converting a random 8bit integer to a string 
  """
  result = ""
  print("randomizing")
  for i in range(0, size):
    ran = random.getrandbits(8)
    result += chr(ran)
  sys.stdout.write(result)
  ## termination string
  sys.stdout.write('##END##')
  return result

def getTotalEntropy(chars):
  ValCount = [0 for b in range(257)];
  entropy = 0
  # can start at total = 1 because 1/1 = 1
  total = 1
  for i in chars:
    ValCount[ord(i)] += 1
    iterations = ValCount[ord(i)]
    px = iterations/total
    mx = math.log2(iterations/total)
    entropy -= (px * mx)
    total += 1
  return entropy

def perfect_eight():
  """ keep randomizing data until entropy returns 8
      if the probability is representing a fitness score	
  """
  for i in range(256):
    result = ""
    for j in range(0, i):
      result += chr(random.getrandbits(8))
    if abs(8-getTotalEntropy(result))<=0.5:
      print('Within ' + str(8-getTotalEntropy(result)) + ' of target entropy\n '
            + 'found at -->' +str(i))
      break
  


# the following code is provided to you for free
if __name__ == "__main__":
  print("type: generate.py random ####### | python3 entropy.py")
  try:
    which = sys.argv[1]
    if which == "random":
      size = int(sys.argv[2])
      random_data(size)
    elif which == "perfect":
      perfect_eight()
    else:
      raise IndexError("invalid option")
  except IndexError as e:
    usage_str = "Usage:\n"                 \
                "\tpython3 {prog} random <size>\n" \
                "\tpython3 {prog} perfect\n"
    sys.stderr.write(usage_str.format(prog=sys.argv[0]))
    sys.exit(1)



