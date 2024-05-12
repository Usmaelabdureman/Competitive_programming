from math import log2
def almostPrime(n):
    factors = []
    
    d = 2
    while d*d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    
    return set(factors)

n = int(input())
ans = 0
for i in range(n+1):
    
    if len(almostPrime(i)) == 2:
        ans += 1
print(ans)

# Implement the lcm 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
