def pcheckr(a):
    """Returns the given number if it is a prime number or 0 if non-prime"""
    i = 2
    for i in range(i, a):
        if a%i==0:
            return 0
        i+=1   
    return a 


def ptest(): 
    """Prints out the first 1000 prime numbers"""
    a = 2
    b = 1
    while a < 7920: #it is as limited, because the 1000th prime number is 7919. I do not need further.
        if pcheckr(a) != 0:
            print b,'th prime is',pcheckr(a)
            b += 1
        a += 1
       


def nthprime(n):
        """Gives the any given up to 1000 n th prime number, starting from 2"""
        a = 2
        b = 1
        while a < 7920:
            if pcheckr(a) != 0:
                if n == b:
                    print b,'th prime is',pcheckr(a)
                b += 1
            a += 1
