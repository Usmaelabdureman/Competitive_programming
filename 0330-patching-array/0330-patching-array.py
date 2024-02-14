class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        i = 0
        cumSum = 0
        
        while cumSum < n:
            
            if i < len(nums) and nums[i] <= cumSum + 1:
                cumSum += nums[i]
                i += 1
            else:
                cumSum += cumSum + 1
                ans += 1
        
        return ans