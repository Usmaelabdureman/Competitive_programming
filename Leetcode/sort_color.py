class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range (1,len(nums)):
            for j in range(len(nums)-i):
                if nums[j]>nums[j+1]:  
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums