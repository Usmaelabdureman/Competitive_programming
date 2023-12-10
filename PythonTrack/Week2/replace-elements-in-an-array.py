class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        ans_dict={}
        for old_value,new_value in reversed(operations):
            ans_dict[old_value]=ans_dict.get(new_value,new_value)
        for indx,value in enumerate(nums):
            if value in ans_dict:
                nums[indx]=ans_dict[value]
        return nums