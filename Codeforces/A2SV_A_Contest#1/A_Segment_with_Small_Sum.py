
n , s = map(int,input().split())
a = list(map(int,input().split()))
left ,right = 0 , 0
ans = n+1

while right < n:
    if s > sum(a[left:right+1]):
        right += 1
    else:
        ans = min(ans, right-left+1)
        left += 1
        
if ans == n+1:  
    print(0)
else:
    print(ans + 1)