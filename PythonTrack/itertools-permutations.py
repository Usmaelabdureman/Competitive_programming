from itertools import permutations
S,r =input().split()
perms = sorted(list(permutations(S, int(r))))
for perm in perms:
    print(''.join(perm))
