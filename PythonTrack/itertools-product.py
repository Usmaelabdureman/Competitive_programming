from itertools import product
A = set(map(int,input().split()))
B = map(int,input().split())
ans=product(A,B)
for a in ans:
    print(a,end=' ')

