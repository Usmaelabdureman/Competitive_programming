class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert the list of stones into a max heap (negate the values to simulate max heap behavior)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            # Get the two heaviest stones
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            # If the stones are not equal, create a new stone with the difference and add it back to the heap
            if x != y:
                heapq.heappush(max_heap, y - x)

        # If there is a stone left, return its weight (negate it back to positive)
        return -max_heap[0] if max_heap else 0


