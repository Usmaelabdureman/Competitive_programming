s = input()
m = int(input())


pref = [0] * (len(s)+1)

for i in range(1,len(s)):
    pref[i] = pref[i-1]  + (s[i-1] == s[i])

for _ in range(m):
    l, r = map(int, input().split())
    count = pref[r-1] - pref[l-1]
    print(count)