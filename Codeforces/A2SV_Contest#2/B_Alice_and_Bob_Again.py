
t=int(input())
for _ in range(t):
    s=input()
    ans=""
    for i in range(len(s)):
        if i%2==0:
            ans+=s[i]
    print(ans+s[-1])
        
        