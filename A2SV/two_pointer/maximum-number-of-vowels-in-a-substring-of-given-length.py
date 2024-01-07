class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_window = window = sum(ch in vowels for ch in s[:k])
        for i in range(k, len(s)):
            window -= s[i - k] in vowels
            window += s[i] in vowels
            max_window = max(max_window, window)
        return max_window