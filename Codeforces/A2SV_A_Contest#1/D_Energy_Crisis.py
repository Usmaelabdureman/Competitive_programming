import sys
n, k = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

def chekcker(x):
    gain = 0
    need = 0
    for num in nums:
        if num > x:
            diff = num - x
            gain += (diff - diff * k / 100)
        if num < x:
            need  += (x - num)
    
    return gain >= need

low = min(nums)
high = max(nums)
while high  - low > 10 ** -7:
    mid = (high + low) / 2
    if chekcker(mid):
        low = mid
    else:
        high = mid
print(high)
