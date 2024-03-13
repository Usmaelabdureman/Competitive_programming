class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        n = len(letters)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if left < n:
            return letters[left]
        else:
            return letters[0]