def gcd (a,b):
    if a < 0 or b < 0: #if numbers are negative
        raise ValueError ("Negative!")
    if b == 0: #nothing can be divided by 0
        return a

    return gcd (b, a%b)

GCD = gcd (12, 16 )
print(GCD) #output : 4