class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_arr=len(nums)
        k=k%len_arr
        left=0
        right=len_arr-1
        while  left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        left=0
        right=k-1
        while  left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        left=k
        right=len_arr-1
        while  left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
            