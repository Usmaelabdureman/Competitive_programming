class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Sort banned array to enable binary search
        banned.sort()
        count = 0

        # Try each number from 1 to n
        for num in range(1, n + 1):
            # Skip if number is in banned array
            if self._custom_binary_search(banned, num):
                continue

            maxSum -= num
            # Break if sum exceeds our limit
            if maxSum < 0:
                break

            count += 1

        return count

    def _custom_binary_search(self, arr: List[int], target: int) -> bool:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False