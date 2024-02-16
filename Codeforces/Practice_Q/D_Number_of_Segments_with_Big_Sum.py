n ,s = map(int,input().split())
arr = list(map(int,input().split()))
left =0
curr_sum=0
big_sum=n+1
for right in range(n):
    curr_sum+=arr[right]
    while curr_sum-arr[left] >=s:
        curr_sum-=arr[left]
        left+=1
if curr_sum >=s:
    big_sum=min(big_sum,right-left+1)
print(big_sum)