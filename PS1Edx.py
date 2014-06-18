#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl'
#Your program should print: Number of vowels: 5

s = 'azcbobobegghakl'
result = 0
for e in s:
    if e in 'aeiou':
        result += 1
    return 'Number of vowels: '+result
