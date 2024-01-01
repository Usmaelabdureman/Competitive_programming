class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2+point[1]**2
        points.sort(key=distance)
        return points[:k]