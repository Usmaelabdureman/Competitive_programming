class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        res=[]
        while left <= right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                res.append(nums[left]*nums[left])
                left+=1
            else:
                res.append(nums[right]*nums[right])
                right-=1
        return res[::-1]
