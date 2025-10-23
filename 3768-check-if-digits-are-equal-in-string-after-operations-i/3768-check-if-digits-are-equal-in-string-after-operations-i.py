class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        s_list = list(s)
        for i in range(1, n - 1):
            for j in range(n - i):
                digit1 = ord(s_list[j]) - ord("0")
                digit2 = ord(s_list[j + 1]) - ord("0")
                s_list[j] = chr(((digit1 + digit2) % 10) + ord("0"))
        return s_list[0] == s_list[1]