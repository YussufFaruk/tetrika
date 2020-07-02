from math import factorial

def get_zeros(n) :
    f = factorial(n)
    k = 0
    sf = str(f)[::-1]
    for i in range(len(sf)) :
        if sf[i] == '0' :
            k += 1
        else :
            break
    return k

print(get_zeros(12))
