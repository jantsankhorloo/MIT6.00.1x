def isWordGuessed(secretWord, lettersGuessed):
    result = ""
    for e in secretWord:
        if e in lettersGuessed:
            result += e
        else:
            result += '_'
            result += ' '
    return result
            
            
        
