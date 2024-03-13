
def LongestEvenOddSubarray(nums, n):
    res = 1
    curr = 1
    if len(nums) == 1 and nums[0] % 2 == 0:
        return 1
    
    
    for i in range(1, n):
        if (nums[i] % 2 == 0 and nums[i-1] % 2 != 0) or (nums[i] % 2 != 0 and nums[i-1] % 2 == 0):
            curr += 1
            res = max(res, curr)
        else:
            curr = 1
    return res                   