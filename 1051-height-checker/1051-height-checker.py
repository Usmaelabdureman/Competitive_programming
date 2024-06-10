class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        cnt = 0
        sorted_h = sorted(heights)

        for i in range(n):
            if heights[i] != sorted_h[i] :
                cnt += 1
        return cnt
