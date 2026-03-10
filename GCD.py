def gcd(a,b):
    # it is a algorithm
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(15,50))
print(lcm(15,50))