def isPalindrome(s): #the input must be a string!
    """Returns True if s is a Palindrome and False otherwise"""
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])  
    
def fib(x):
    """Returns fibonacci of x, where x is non-negative int"""
    if x == 0 or x == 1: return 1
    else: return fib(x-1)+fib(x-2)