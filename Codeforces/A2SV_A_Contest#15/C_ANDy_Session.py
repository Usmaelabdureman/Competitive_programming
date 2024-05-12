t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    current_and = (1 << 31) - 1 
     
    for num in a:
        current_and &= num
        
    # print(a, current_and)
    
    for j in range(30, -1, -1):
        mask = 1 << j
        needed = 0
        for num in a:
            if num & mask == 0:
                needed += 1
        if needed <= k:
            ans |= mask
            k -= needed
        else:
            ans |= (current_and & mask)

    print(ans)