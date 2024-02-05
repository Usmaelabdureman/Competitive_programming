n = int(input())
a = list(map(int, input().split()))

max_score = 1000
count = [0] * (max_score + 1)
for i in a:
    count[i] += 1

max_freq = max(count)
res = 0

for _ in range(max_freq):
    cnt = 0
    for i in range(max_score + 1):
        if count[i] > 0:
            count[i] -= 1
            cnt += 1
    if cnt > 0:
        res += cnt - 1

print(res)