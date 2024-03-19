#  Beautiful Union Codeforces Round #731 (Div. 3)
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_min = min(a)
    b_min = min(b)
    ans = 0
    for i in range(n):
        ans += max(a[i] - a_min, b[i] - b_min)
    print(ans)
    