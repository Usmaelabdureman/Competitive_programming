class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeroes=nums.count(0)
        # for elt in nums:
        #     if elt == 0:
        #         nums.remove(elt)
        #     else:
        #         continue
        # nums.extend([0]*zeroes)
        left=0
        right=0
        while right<len(nums):
            if nums[right] != 0:
                nums[right],nums[left]=nums[left],nums[right]
                left+=1
            right+=1
        
                