t = int(input())
res = []
for i in range(t):
    a, b, c = map(int, input().split())
    res.append(sorted([a, b, c])[1])
for r in res:
    print(r)
