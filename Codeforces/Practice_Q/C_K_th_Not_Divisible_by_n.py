

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    low = 0
    high = n * k
    
    while high - low > 1:
        mid = (low + high) // 2
        total_divisible = mid // n
        
        non_div_cnt = mid - total_divisible
        
        if non_div_cnt < k:
            low = mid 
        else:
            high = mid
    print(high)
