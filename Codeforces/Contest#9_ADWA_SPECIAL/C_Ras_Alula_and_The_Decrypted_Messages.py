
t = int(input())
for _ in range(t):
    N, M = map(int,input().split())
    s = input()
    w = input()

    target = 0
    window_sum = 0
    for i in range(M):
        target += ord(w[i])
        window_sum += ord(s[i])
    
    found = False
    for i in range(M, N):
        if window_sum == target:
            found = True
            break
        window_sum += ord(s[i])
        window_sum -= ord(s[i - M])
    
    if window_sum == target or found:
        print("YES")
    else:
        print("NO")