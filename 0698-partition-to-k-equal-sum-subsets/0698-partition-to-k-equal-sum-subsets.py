class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total_sum = sum(nums)
        target_sum = total_sum // k
        
        if total_sum % k != 0 or max(nums) > target_sum:
            return False
        
        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        
        subset_sum = [0] * (1 << n)
        
        for mask in range(1 << n):
            if not dp[mask]:
                continue
                
            for i in range(n):
                next_mask = mask | (1 << i)
                if mask & (1 << i) == 0 and subset_sum[mask] % target_sum + nums[i] <= target_sum:
                    dp[next_mask] = True
                    subset_sum[next_mask] = subset_sum[mask] + nums[i]
        
        return dp[(1 << n) - 1]