from itertools import combinations
s, k = input().split()
s = sorted(s)
for i in range(1, int(k)+1):
    for c in combinations(s, i):
        print(''.join(c))
