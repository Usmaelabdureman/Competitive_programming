
n, k = map(int,input().split())

arr = list(map(int,input().split()))


def helper(cap):
    seg = 1
    total = 0
    
    for a in arr:
        total += a
        
        if total > cap:
            total = a
            seg += 1
        if seg > k:
            return False
    return True
    
low = max(arr) 
high = sum(arr)

while low <= high:
    
    cap = (low + high)//2
    if helper(cap):
        high = cap - 1
    else:
        low = cap + 1
print(low)