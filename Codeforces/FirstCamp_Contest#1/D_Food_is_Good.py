t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    simon_t = sum(a)
    
    aman_t = 0
    count = 0
     
    curr_sum = 0
    for num in a:
        if num >= 0:
            count += 1
        curr_sum += num
        
        if curr_sum < 0:
            curr_sum = 0
        aman_t = max(curr_sum, aman_t)
    
    if count == len(a) or simon_t > aman_t:
        print("YES")
    else:
        print("NO")