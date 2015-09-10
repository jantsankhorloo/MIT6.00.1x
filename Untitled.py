#def printMove(fr,to):
#    print ('move from '+str(fr)+' to '+str(to))

#def towers(n,fr,to,spare):
#    if n == 1:
#        printMove(fr, to)
#    else:
#        towers(n-1,fr,spare,to)
#        towers(1,fr,to,spare)
#        towers(n-1,spare,to,fr)

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in 'qazwsxedcrfvtgbyhnujmikolp':
                ans += c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == [-1] and isPal(s[1:-1])

    return isPal(toChars(s))



def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
    #if aStr == '':
        #return False

   # Base case: if aStr is of length 1, just see if the chars are equal
    #elif len(aStr) == 1:
#        return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character
#    midIndex = len(aStr)/2
#    midChar = aStr[midIndex]
#    if char == midChar:
      # We found the character!
#        return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
#    elif char < midChar:
#        return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
#    else:
#        return isIn(char, aStr[midIndex:])



def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # If strings aren't the same length, they cannot be semordnilap
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1:
        return str1 == str2

    # Recursive case: check if the first letter of str1 equals the last letter
    # of str2
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)



#L = [1,-2,3.4]
def applytoEach(L,f):
    """assumes L is a list, f a function
        mutates L by replacing each element,
        e, of L by f(e)"""
    for i in range (len(L)):
        L[i] = f(L[i])

def applyFuns(L,x):
    for f in L:
        print (f(x))

applyFuns([abs,int],4)
        
        
    
    
