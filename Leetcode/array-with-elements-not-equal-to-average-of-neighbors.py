class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort() #sort numbers
        len_num=len(nums)
        for i in range(0,len_num-1,2): 
            nums[i],nums[i+1]= nums[i+1], nums[i]
        return nums