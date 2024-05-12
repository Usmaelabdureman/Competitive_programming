from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] > right[j]:  # Note the greater than sign for descending order
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result += left[i:]
            result += right[j:]
            return result
        sorted_nums = merge_sort(nums)  
        return sorted_nums[k - 1]


# Example usage
nums = [5, 2, 4, 1, 3]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))  