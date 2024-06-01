class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(1,n):
            first = ord(s[i-1]) - ord('a')
            second =  ord(s[i]) - ord('a')
            ans += abs(second - first)
        return ans