n,m = map(int,input().split())

list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list1.append(float('inf'))

left=0
right=0
ans=[]
while left<len(list1) and right<len(list2):
    if list1[left]<=list2[right]:
        ans.append(list1[left])
        left+=1
    else:
        ans.append(list2[right])
        right+=1
# ans.extend(list1[left:])
# ans.extend(list2[right:])
print(*ans)