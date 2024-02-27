
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    
    for i in range(n):
        if a[i] != b[i] and a[i] % 2 != b[i] % 2:
            print("NO")
            break
    else:
        print("YES")