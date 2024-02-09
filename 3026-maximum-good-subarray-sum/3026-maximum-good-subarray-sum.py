class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_sum=0
        ans = -inf
        pref_sum={nums[0]:0}
        
        for i,num in enumerate(nums):
            cur_sum += num
            
            if num - k in pref_sum:
                ans = max(ans,cur_sum-pref_sum[num - k])
                
            if num + k in pref_sum:
                ans = max(ans,cur_sum-pref_sum[num + k])
                
            if i+1 < n and (nums[i+1] not in pref_sum or pref_sum[nums[i+1]] > cur_sum):
                pref_sum[nums[i+1]] = cur_sum
        return ans if ans !=-inf else 0
                