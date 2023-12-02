n=int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans=0
for i in range(1,n):
    ans+=a[0]-a[i]
print(ans)