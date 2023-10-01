class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_arr=len(nums)
        left=0
        subarraySum=0
        ans=float('inf')
        for right in range(len_arr):
            subarraySum+=nums[right]
            while subarraySum>=target:
                ans=min(right-left+1,ans)
                subarraySum-=nums[left]
                left+=1
        return 0 if ans==float('inf') else ans