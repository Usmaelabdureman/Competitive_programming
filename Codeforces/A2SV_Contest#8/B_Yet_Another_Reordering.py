from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

for num in a:
    d[num] += 1

sortd_nums = sorted(d.keys(), key=lambda x: d[x], reverse=True)

max_pos = 0
curr_pos = 0

for num in sortd_nums:
    max_pos += min(d[num], curr_pos)
    curr_pos += d[num]
print(max_pos)
