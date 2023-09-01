class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1 == 0:
                ans[i] = ans[i >> 1]
            else:
                ans[i] = ans[i - 1] + 1
        return ans
