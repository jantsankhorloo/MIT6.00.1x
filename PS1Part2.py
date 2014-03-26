def pcheckr(a):
    """prime number checker"""
    i = 2
    for i in range(i, a):
        if a%i==0:
            return 0
        i+=1   
    return a 
    
    
    
def upto(m):
    """up to any number m"""
    a = 2
    b = 1
    while b <= m:
        if pcheckr(a) != 0:
            print b, '=', pcheckr(a)
            b+=1
        a+=1


#computes the sum of the logarithms of all the primes from 2 to some 
#number n, and print out the sum of the logs of the primes, the number n, and the ratio of these 
#two quantities    
     
def log(m):
    s = 0
    a = 2
    b = 1
    while b <= m:
        if pcheckr(a) != 0:
            import math
            s = s + math.log(a)
            b+=1
        a+=1
    print (s, m, (s/m))
