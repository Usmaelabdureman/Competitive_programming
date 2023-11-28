class Solution:
    def twoSum(self, nums, target):
        lst={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in lst:
                return [lst[diff],i]
            lst[nums[i]]=i