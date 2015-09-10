def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    total = 0.0;
    k = start;
    while(k<stop):
        total += step * f(k);
        k = k + step;
    return total;
    
