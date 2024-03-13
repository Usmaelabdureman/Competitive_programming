n, q = map(int, input().split())

price = list(map(int, input().split()))
price.sort(reverse=True)

pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + price[i - 1]

for _ in range(q):
    x, y = map(int, input().split())
    print(pref[x] - pref[x - y])
