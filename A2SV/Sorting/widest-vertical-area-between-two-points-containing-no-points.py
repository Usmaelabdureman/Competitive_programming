class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans=0
        points.sort(key=lambda x:x[0])
        for i in range(1,len(points)):
            ans=max(ans,points[i][0]-points[i-1][0])
        return ans