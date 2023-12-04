class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance=sum(distance)
        if start > destination:
            start,destination=destination,start
        cw_distance=sum(distance[start:destination])
        ccw_distance=total_distance-cw_distance
        return min(cw_distance,ccw_distance)
        