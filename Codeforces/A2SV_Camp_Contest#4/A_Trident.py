
t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = list(map(int,input().split()))
    
    i,j = 0,1
    ans = []
    for k in range(2,n):
        if i < j < k and arr[i]<arr[j] and arr[j]>arr[k]:
            ans.extend([i+1,j+1,k+1])
            # break
        i += 1
        j += 1
    if ans:
        print("YES")
       
        print(*ans)
    else:
        print("NO")
  
    
    