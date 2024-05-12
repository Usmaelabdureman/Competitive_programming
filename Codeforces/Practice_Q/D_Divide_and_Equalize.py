def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def solve(n, arr):
    factors = {}
    for a in arr:
        for f in factorize(a):
            factors[f] = factors.get(f, 0) + 1
    for f in factors:
        if factors[f] % n:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))