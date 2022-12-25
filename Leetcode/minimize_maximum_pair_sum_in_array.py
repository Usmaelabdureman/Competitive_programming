class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        maxSum=0
        while l<r:
            temp=nums[l]+nums[r]
            maxSum=max(maxSum,temp)
            l+=1
            r-=1
        return maxSum