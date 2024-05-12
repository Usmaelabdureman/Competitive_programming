n, t = map(int, input().split())
a = list(map(int, input().split()))

r = 0
min_ = 0
ans = 0
for i in range(n):
    while r < n and min_ + a[r] <= t:
        min_ += a[r]
        r += 1
    ans = max(ans, r - i)
    min_ -= a[i]

print(ans)
