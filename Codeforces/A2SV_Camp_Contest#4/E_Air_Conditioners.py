t = int(input())

for _ in range(t):
    
    input()
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c = [float('inf')] * n
    for i in range(k):
        c[a[i] - 1] = t[i]

    p = float('inf')
    L = [float('inf')] * n
    
    for i in range(n):
        p = min(p + 1, c[i])
        L[i] = p

    p = float('inf')
    R = [float('inf')] * n
    for i in range(n - 1, -1, -1):
        p = min(p + 1, c[i])
        R[i] = p

    for i in range(n):
        print(min(L[i], R[i]), end=" ")
    print()

# q = int(input())

# for _ in range(q):
#     n,k = map(int,input().split())
#     pos = list(map(int,input().split()))
#     temp = list(map(int,input().split()))
    

