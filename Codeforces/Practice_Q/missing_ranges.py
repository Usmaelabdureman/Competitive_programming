from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[lower, upper]]
        
        if nums[0] > lower:
            res.append([lower, nums[0] - 1])
        
        for a,b in zip(nums, nums[1:]):
            if b - a > 1:
                res.append([a + 1, b - 1])
                
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
        return res
            
    
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
s = Solution()
print(s.findMissingRanges(nums, lower, upper))
