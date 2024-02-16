n ,s = map(int,input().split())
arr = list(map(int,input().split()))
left =0
ans=0
min_val = float('inf')
max_val=float('-inf')
for right in range(n):
    min_val = min(min_val,arr[right])
    max_val = max(max_val,arr[right])
    while max_val -min_val > s:
        left+=1
        min_val = min(arr[left:right + 1])
        max_val = max(arr[left:right + 1])
    ans+=right-left+1
print(ans)
    