# Networking Labs 2017

These were a set of labs that I really enjoyed.

### Lab 4
**What is the maximum possible entropy for data of `base64` encoding?**
  >> The max possible entropy would occur when a string of characters length 256 each had "unique" occurences of each character.
  >> This means that if each character only appeared once, then the probability of each would be 1/256 (in UTF8). Since we are mulitplying fractions
  >> the bigger the difference between the numerator and denominator, the bigger the probability ==> the bigger the entropy will be.
  	With this calculation, the max entropy would be slightly different since base64 is restricted to less characters than all 256 unique characters
   	that UTF-8 can map to. This means if we are restricted to 64 bits, our max entropy would be 64. 

**Derive a general formula for getting maximum entropy**
	 `   $H(X) = -\sum_{\forall i} (P(x_i)* lg(P(x_i))) $`

  >> As stated in problem 1, since we are restricted to n characters, the max entropy occurs when we have exactly
  >> n items each unique. This means that we can use the general form: 
   ```LaTeX
    -\sum (1/n) * (log2(1\n)) 
   ```


### Lab 6
Aaron$ time python3 generate.py random 22 | python3 entropy.py 
        0.04 real         0.03 user         0.00 sys
23.465060517096568

Aaron$ time python3 generate.py perfect entropy.py 
Within 0.17695470881825326 of target entropy
found at -->25

Aaron$ time python3 generate.py random 25 entropy.py 
randomizing..
ÒèRM Pß4àvB¶ÚJìUa÷ÑÚ££END££
real	0m0.054s
user	0m0.036s
sys	0m0.010s

Aaron$ time python3 generate.py random 25 entropy.py 
randomizing..
¹®:°.°.°-ÈáN´¶¶¢µ0¢¢>££END££
real	0m0.052s
user	0m0.035s
sys	0m0.010s

Aaron$ time python3 generate.py random 25 entropy.py 
randomizing..
R1ëÛyYwhòæQaÀ£	ÏàÁBèN££END££
real	0m0.055s
user	0m0.038s
sys	0m0.010s

