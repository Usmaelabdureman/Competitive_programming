n ,s = map(int,input().split())
arr = list(map(int,input().split()))

left =0
longest =0
curr_sum=0
# while right < n:
#     curr_sum+=arr[right]
#     while curr_sum > s:
#         curr_sum-=arr[left]
#         left+=1
#     right+=1
#     longest=max(longest,right-left)
# print(longest)

for right in range(n):
    curr_sum+=arr[right]
    while curr_sum > s:
        curr_sum-=arr[left]
        left+=1
    longest = max(longest,right-left+1)
print(longest)
        
    