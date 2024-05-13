class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = [0] * len(nums)
        
        def dp(i):
            if i == len(nums):
                return 0
            if memo[i] == 0:
                memo[i] = 1
                for j in range(i):
                    if nums[i] > nums[j]:
                        memo[i] = max(memo[i],dp(j)+1)
            return memo[i]
        return max(dp(i) for i in range(len(nums)))