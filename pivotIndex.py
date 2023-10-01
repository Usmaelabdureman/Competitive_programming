class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftSum=0
        for i ,j in enumerate(nums):
            if leftSum==(total-leftSum-j):
                return i
            leftSum+=j
        return -1