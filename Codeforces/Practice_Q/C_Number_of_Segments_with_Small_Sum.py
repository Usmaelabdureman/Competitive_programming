
n ,s = map(int,input().split())
arr = list(map(int,input().split()))

total=0
curr_sum=0
left=0
for right in range(n):
    curr_sum+=arr[right]
    while curr_sum > s:
        curr_sum-=arr[left]
        left+=1
    total+=right-left+1
print(total)