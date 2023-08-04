import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        
        heap = []
        for point in points:
            dist = distance(point)
            heapq.heappush(heap, (dist, point))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
