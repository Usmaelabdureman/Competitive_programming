n, k, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

groups = 1
gaps = []

for i in range(1, n):
    if a[i] - a[i-1] > x:
        gaps.append((a[i] - a[i-1] - 1) // x)
    
gaps.sort()

for gap in gaps:
    if k >= gap:
        k -= gap
    else:
        groups += 1

print(groups)

