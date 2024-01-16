class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_sub = 0
        current_sum = 0
        seen = set()

        while right < len(nums):
            if nums[right] not in seen:
                current_sum += nums[right]
                max_sub = max(max_sub, current_sum)
                seen.add(nums[right])
                right += 1
            else:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

        return max_sub
