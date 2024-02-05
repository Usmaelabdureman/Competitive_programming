t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    # b.sort()
    a = [b[0]]

    for i in range(n-1):
        a.append(min(a[i - 1], b[i]+a[i-1] ))
    print(*a)