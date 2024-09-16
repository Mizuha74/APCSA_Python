def gcd(a,b):
    if a > b: # x is big, y is small, r is reminder, g is gcd
        x = a
        y = b
    else:
        x = b
        y = a
    r = x % y
    
    while r > 0:
        print (x,y,r)
        x = y
        y = r
        r = y % r
    return y
    
print(gcd(72,26))

