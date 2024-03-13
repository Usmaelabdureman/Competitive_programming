class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        left = 0
        ans = int(nums[0] % 2 == 0 and nums[0] <= threshold)
        n = len(nums)

        for right in range(n):
            if nums[left] % 2 != 0 or nums[left] > threshold \
            or nums[right] > threshold \
            or (right and nums[right] % 2 == nums[right - 1] % 2):
                left = right

            if nums[left] % 2 == 0 and nums[left] <= threshold:
                ans = max(ans, right - left + 1)

        return ans