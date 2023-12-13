t= int(input())
for _ in range(t):
    n= int(input())
    a= list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i+2,n):
            if a[i]==a[j]:
                ans=1
                break
        if ans==1:
            break
    if ans==1:
        print("YES")
    else:
        print("NO")