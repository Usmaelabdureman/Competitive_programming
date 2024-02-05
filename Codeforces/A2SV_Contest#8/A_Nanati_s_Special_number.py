from collections import defaultdict
t = int(input())
for  _ in range(t):
    n = int(input())
    s = input()
    d= defaultdict(int)
    for char in s:
        d[char] = ord(char)-ord('a')+1
    print(max(d.values()))
