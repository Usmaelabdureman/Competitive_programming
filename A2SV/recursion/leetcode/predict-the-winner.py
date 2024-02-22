class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def recur(start, end):
            if start > end:
                return 0
            startingVal, endingVal = nums[start], nums[end]
            left = recur(start + 1, end)
            right = recur(start, end - 1)
            return max(startingVal - left, endingVal - right)
        return recur(0, len(nums) - 1) >= 0
        
        