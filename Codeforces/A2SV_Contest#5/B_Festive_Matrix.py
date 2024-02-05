n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans=0
for i in range(n):
    ans+=a[i][i]
    ans+=a[i][n-i-1]
    ans+=a[n//2][i]
    ans+=a[i][n//2]
# remove double counting of the middle row and column
ans-=3*a[n//2][n//2]
print(ans)
