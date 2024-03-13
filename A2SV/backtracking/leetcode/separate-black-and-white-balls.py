class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        ans = 0
        count = 0
       
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                count += 1
                ans += n - i - count
        return ans
