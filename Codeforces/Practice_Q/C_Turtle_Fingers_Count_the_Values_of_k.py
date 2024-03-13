
t = int(input())

for _ in range(t):
    a,b,l = map(int,input().split())
    
    cnt  = 0
    for i in range(1,l+1):
        if l%a == 0 and l%b == 0:
            if l%i == 0:
                cnt +=1 
    print(cnt)