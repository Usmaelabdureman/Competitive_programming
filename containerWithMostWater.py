class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            width=right-left
            res = max(res, min(height[left], height[right]) *width)
            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
        return res