class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        # 
        for c in s:
            count[c] += 1
        # 
        if all(v <= n // 4 for v in count.values()):
            return 0
        # 
        ans, j = n, 0
        for i, c in enumerate(s):
            count[c] -= 1
            while j <= i and all(v <= n // 4 for v in count.values()):
                ans = min(ans, i - j + 1)
                count[s[j]] += 1
                j += 1
        return ans