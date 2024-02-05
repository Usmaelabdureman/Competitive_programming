n,m = map(int,input().split())

list1=list(map(int,input().split()))
list2=list(map(int,input().split()))


ans=[]
left=0

for right in range(len(list2)):
    while left<len(list1) and list1[left]<list2[right] :
        left+=1
    ans.append(left)
print(*ans)
        
   
