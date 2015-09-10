def count(n):
    a = 0
    b = 0
    c = 0
    for a in range(n/20):
        for b in range(n/9):
            for c in range(n/6):
                calc(a,b,c,n)
                c+=1
            b+=1
        a+=1
                
                
        


def calc(a,b,c,n):
    if ((20*a+9*b+6*c) == n):
        print (a, b, c)
        