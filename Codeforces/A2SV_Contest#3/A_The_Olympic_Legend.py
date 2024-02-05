t=int(input())
for _ in range(t):
    distances= list(map(int,input().split()))
    cnt=0
    for i in range(1,4):
        if distances[i]>distances[0]:
            cnt+=1
    print(cnt)
        
    
    