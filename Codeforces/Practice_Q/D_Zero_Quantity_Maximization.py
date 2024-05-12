from collections import defaultdict
from fractions import Fraction

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dict_ratio = defaultdict(int)
zeroes = 0

for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            zeroes += 1
    else:
        ratio = -Fraction(b[i], a[i])  
        dict_ratio[ratio] += 1
        
print(dict_ratio)
print(max(dict_ratio.values(), default=0) + zeroes)
