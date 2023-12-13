t=int(input())
set1='codeforces'

for _ in range(t):
    s=input()
    ans=0
    for i in range(len(s)):
        if s[i]!=set1[i]:
            ans+=1
    print(ans)