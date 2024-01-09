class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        zeroes_count=0
        longest_subarray=0
        left =0
        for right in range(n):
            zeroes_count+=(nums[right]==0)
            while zeroes_count > 1:
                zeroes_count-=(nums[left]==0)
                left+=1
            longest_subarray = max(longest_subarray,right-left)
        return longest_subarray
