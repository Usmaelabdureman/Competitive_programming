t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    ans =[]
    sorted_v = sorted(s)
    for i in range(n):
        if s[i] != max(s):
            ans.append(s[i]-sorted_v[-1])
        else:
            ans.append(sorted_v[-1]-sorted_v[-2])
    print(*ans)