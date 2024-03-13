
from itertools import accumulate


n = int(input())
t = list(map(int,input().split()))

pref = list(accumulate(t))
count = 0

for i in range(len(t)):
    if pref[i] > t[i]:
        count += 1
print(count)