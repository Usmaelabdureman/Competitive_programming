
n , k = map(int, input().split())

stalls = list(map(int, input().split()))

def helper(dist):
    cow = 1
    sum_stalls = 0
    
    for stall in stalls:
        sum_stalls += stall
        
        if sum_stalls > dist:
            cow += 1
            sum_stalls = stall
        if cow > k:
            return False
    return True
    
low = 0
high = 10**9

while low < high:
   
   mid = (low + high)//2
   
   if helper(mid):
       high = mid - 1
   else:
       low = mid + 1
print(low)
   
   