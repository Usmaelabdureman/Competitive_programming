class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i - 2: i])
                i -= 3
            else:
                num = int(s[i])
                i -= 1
            result = chr(ord('a') + num - 1) + result
        return result
