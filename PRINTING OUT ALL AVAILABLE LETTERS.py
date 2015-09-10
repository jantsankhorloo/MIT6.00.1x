def getAvailableLetters(lettersGuessed):
    import string
    alph = string.ascii_lowercase
    for e in lettersGuessed:
        if e in alph:
            alph = alph.replace(e,"")
    return alph
            
            
