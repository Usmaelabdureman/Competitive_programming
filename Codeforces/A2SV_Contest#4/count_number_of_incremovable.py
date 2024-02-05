# from typing import List
# class Solution:
#     def incremovableSubarrayCount(self, nums: List[int]) -> int:
#         count = 0
#         n = len(nums)
        
#         for i in range(n):
#             for j in range(i, n):
#                 remaining = nums[:i] + nums[j+1:]
#                 if all(remaining[k] < remaining[k+1] for k in range(len(remaining)-1)):
#                     count += 1
        
#         return count
# test = Solution()
# print(test.incremovableSubarrayCount([1,2,3,4]))
# print(test.incremovableSubarrayCount([6,5,7,8]))
# print(test.incremovableSubarrayCount([8,7,6,6]))

arr = [1, 2, 0, 3,8,9,88, 4, 3, 0, 0, 0, 1, 3,-5,-6, 4]

max_num = max(arr)
min_num = min(arr)

count = [0] * (max_num - min_num + 1)
for i in range(len(arr)):
    count[arr[i] - min_num] += 1

sorted_arr = []
for i in range(len(count)):
    sorted_arr.extend([i + min_num] * count[i])
print(sorted_arr)