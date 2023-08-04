class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda k:k[0]**2+k[1]**2)
        return points[:k]