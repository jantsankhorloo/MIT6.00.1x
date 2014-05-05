def isPalindrome(s): #the input must be a string!
    """Returns True if s is a Palindrome and False otherwise"""
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])  
    
def fib(x): #on x == 36, it takes a while to calculate. Patience, young grasshopper!
    """Returns fibonacci of x, where x is non-negative int"""
    if x == 0 or x == 1: return 1 #Base
    else: return fib(x-1)+fib(x-2) #Recursive
    
def fib_interative(x):
    """Iterative version of fibonacci algorithm""" 
    current = 0 
    after = 1
    for i in range(0, x):
        current, after = after, current + after
    return current
