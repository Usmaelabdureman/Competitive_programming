class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)

        zeroes = s.count("0")
        ones = n - zeroes
        count_zero = 0
        count_one = 0
        ans = 0
        for c in s:
            if c == "0":
                ans += count_one * (ones - count_one)
                count_zero += 1
            else:
                ans += count_zero * (zeroes - count_zero)
                count_one += 1
        return ans