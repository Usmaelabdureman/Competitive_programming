from itertools import pairwise
from math import gcd
# Small GCD

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for a, b in pairwise(arr):
        ans += gcd(ans, b)*(n - arr.index(b))
    print(ans)