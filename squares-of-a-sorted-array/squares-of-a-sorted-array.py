class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [i*i for i in nums]
        nums = sorted(nums)
        return nums
        