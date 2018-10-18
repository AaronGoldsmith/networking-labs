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
