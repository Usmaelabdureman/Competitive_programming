from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    c = Counter(s)
    if len(c) == 1:
        print(-1)
    else:
        print(len(s)-1)
    