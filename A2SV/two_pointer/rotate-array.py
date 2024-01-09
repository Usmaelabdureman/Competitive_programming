class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # arr=[0]*len(nums)
        # n=len(nums)
        # for i in range(n):
        #     arr[(i+k)%n]=nums[i]
        # for i in range(n):
        #     nums[i]=arr[i]

        # Two pointer approach
        len_arr=len(nums)
        k=k%len_arr
        left=0
        right=len_arr-1
        # Reversing the last part array
        while  left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

        left=0
        right=k-1
        # reversing the first 
        while  left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        left=k
        right=len_arr-1
        # reversing the whole array
        while  left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1    

