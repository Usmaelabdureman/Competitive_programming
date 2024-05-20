n = int(input())
arr = list(map(int,input().split()))

arr_indx = [[i,num] for i,num in enumerate(arr)]

arr_indx.sort(key = lambda x : x[1])
# print(arr_indx)
ans = []
left = 0
right = n-1

while left < right:
    ans.append([arr_indx[left][0]+1,arr_indx[right][0]+1])
    left += 1
    right -= 1
    
for a in ans:
    print(*a)
