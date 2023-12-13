t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    x = max(a) - min(a)
    if sorted(a) == a:
        print(-1)
    else:
        print(x)