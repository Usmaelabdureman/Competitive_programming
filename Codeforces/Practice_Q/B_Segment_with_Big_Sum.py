n ,s = map(int,input().split())
arr = list(map(int,input().split()))
left =0
curr_sum=0
smallest_length=float('inf')
for right in range(n):
    curr_sum+=arr[right]
    while curr_sum >=s:
        smallest_length=min(smallest_length,right-left+1)
        curr_sum-=arr[left]
        left+=1
print(smallest_length if smallest_length!=float('inf') else -1)
