from typing import List


# class Solution:
#     def incremovableSubarrayCount(self, nums: List[int]) -> int:
#         n = len(nums)
#         left = [1] * n
#         right = [1] * n
#         for i in range(1, n):
#             if nums[i] > nums[i - 1]:
#                 left[i] = left[i - 1] + 1
#         for i in range(n - 2, -1, -1):
#             if nums[i] < nums[i + 1]:
#                 right[i] = right[i + 1] + 1
#         ans = 0
#         for i in range(n):
#             if left[i] > right[i]:
#                 ans += left[i]
#             else:
#                 ans += left[i-n]
#         return ans

from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        count = 0

        for i in range(n):
            while j + 1 < n and nums[j+1] >= nums[j]:
                j += 1
            if j + 1 < n and nums[j+1] == nums[j]:
                continue
            count += j - i + 1

        return count

# our input [1,2,3,4], [6,5,7,8], [8,7,6,6]
test = Solution()
print(test.incremovableSubarrayCount([1,2,3,4]))
print(test.incremovableSubarrayCount([6,5,7,8]))
print(test.incremovableSubarrayCount([8,7,6,6]))