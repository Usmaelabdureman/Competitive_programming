class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc=True
        is_dec=True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                is_inc=False
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                is_dec=False
        return is_inc or is_dec