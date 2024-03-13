shows = []
testc = int(input())

for _ in range(testc):
    start, end = map(int, input().split())
    
    shows.append((start,1))
    shows.append((end+1,-1))
   
shows.sort()
cnt = 0
for event in shows:
    cnt += event[1]  
    if cnt >= 3:
        print("NO")
        break
else:
    print("YES")
