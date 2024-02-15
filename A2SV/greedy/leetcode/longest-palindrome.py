from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        one_char = 0

        for v in counter.values():
            ans += v // 2 * 2
            if v % 2 == 1:
                one_char = 1

        return ans + one_char
