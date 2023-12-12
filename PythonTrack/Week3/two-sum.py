class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_of_nums={}

        for index,num in enumerate(nums):
            diff =target-num
            if diff in dict_of_nums:
                return [dict_of_nums[diff],index]
            dict_of_nums[num]=index