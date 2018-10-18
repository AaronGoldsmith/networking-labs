# Networking Labs 2017

These were a set of labs that I really enjoyed.

### Lab 4
**What is the maximum possible entropy for data of `base64` encoding?**

The max possible entropy would occur when a string of characters length 256 each had "unique" occurences of each character.
  > This means that if each character only appeared once, then the probability of each would be 1/256 (in UTF8). Since we are mulitplying fractions
  > the bigger the difference between the numerator and denominator, the bigger the probability ==> the bigger the entropy will be.
  	With this calculation, the max entropy would be slightly different since base64 is restricted to less characters than all 256 unique characters
   	that UTF-8 can map to. This means if we are restricted to 64 bits, our max entropy would be 64. 

**Derive a general formula for getting maximum entropy**
   ```$H(X) = -\sum_{\forall i} (P(x_i)* lg(P(x_i))) ```
    
> As stated in problem 1, since we are restricted to n characters, the max entropy occurs when we have exactly
>  n items each unique. This means that we can use the general form: 
 

   ``` -\sum (1/n) * (log2(1\n)) ```

### Lab 5
**Why is `chunk_size` and `packet_size` different?**
	-chunk_size is referring to the max number of bytes
	  to be read in each time the recv() function is called
  - packet_size is most likely going to be bigger than chunk_size. Chunk_size should be the "fragments" so to speak
  	  of the data being sent, where as packet_size is total bytes being sent. (Including sequence number, checksum, data)    

**Explain the idea 'checksum' in the context of this lab**
- checksum is used to get the aggregate total number of bits, and then mods it by the size of the packet (so that the maximum number of bits will always be the size of the packet)
    
**What is serialization and deserialization**
- Serialization passes the data into a structure so that we can retrieve it later easily.
- In the lab we use a dictionary because that maps keys and values which is explicitly the reason for JSON payloads returns
   > When we deserialize we can easily reference a specific item in the packet 

**Provide some ideas to modify the code so that we will be able to handle lost messages and missing acknowledgements**
- Implement a "timing function", or TTL (time to live).
- After a certain number of hops, resend the data in case there were any errors
