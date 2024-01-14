class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        left = right = 0
        max_count = 0
        n = len(s)
        while right < n :
            count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[right]) - ord('A')])
            if right - left+1 > max_count+k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            right += 1
        return right -left
