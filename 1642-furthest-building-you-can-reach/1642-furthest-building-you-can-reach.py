class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []  # To store the differences between heights that need bricks
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(min_heap, diff)
            if len(min_heap) > ladders:  # Use ladders for the tallest differences
                bricks -= heapq.heappop(min_heap)
            if bricks < 0:  # If bricks become negative, return the current index
                return i
        return len(heights) - 1  
