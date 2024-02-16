from collections import defaultdict
n ,s = map(int,input().split())
arr = list(map(int,input().split()))
left =0
ans=0
count=defaultdict(int)
for right in range(n):
    count[arr[right]] = count.get(arr[right],0)+1
    while len(count) > s:
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                count.pop(arr[left])
            left += 1
    ans += right - left + 1
print(ans)
    