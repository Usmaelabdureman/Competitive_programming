class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        min_arrows = 0
        end = float('-inf')
        
        for interval in points:
            if interval[0] > end:
                min_arrows += 1
                end = interval[1]
        
        return min_arrows
            