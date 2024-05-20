
from collections import defaultdict

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    primes = [num for num, prime in enumerate(is_prime) if prime]
    
    return primes

def prime_factors(num, primes):
    factors = set()
    for prime in primes:
        if prime * prime > num:
            break
        
        while not(num % prime):
            factors.add(prime)
            num //= prime
            
    if num > 1:
        factors.add(num)
        
    return factors

N = int(input())
arr = list(map(int, input().split()))

max_num = max(arr)
primes = sieve(max_num)

info = []
for num in arr:
    factors = prime_factors(num, primes)
    info.append(factors)
    
dp = defaultdict(int)
ans = 1

for i in range(N - 1, -1, -1):
    curr_max = 1
    for factor in info[i]:
        curr_max = max(curr_max, dp[factor] + 1)
        
    for factor in info[i]:
        dp[factor] = curr_max
        
    ans = max(ans, curr_max)
        
print(ans)
