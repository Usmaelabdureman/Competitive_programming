
n = int(input())
ans=0
for _ in range(n):
    v= list(map(int,input().split()))
    res=[]
    for i in v:
        res.append(i)
    if sum(res)>=2 :
        ans+=1
print(ans)