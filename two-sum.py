class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst={}
        for i,num2 in enumerate(nums):
            diff=target-num2
            if diff in lst:
                return [lst[diff],i]
            lst[num2]=i