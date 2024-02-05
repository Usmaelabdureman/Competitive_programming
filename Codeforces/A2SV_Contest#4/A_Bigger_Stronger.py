
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    distinct=set(a)
    if len(distinct) == len(a):
        print('YES')
    else:
        print('NO')
    