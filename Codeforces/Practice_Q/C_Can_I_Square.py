

def Sqrt(n):
    low = 1
    high = n
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1

    return high

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    
    ans = Sqrt(sum_a)
    
    if ans*ans == sum_a:
        print("YES")
    else:
        print("NO")