class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = [(c,p) for c ,p in zip(capital,profits)]
        heapify(heap)
        heap2 = []
        
        for _ in range(k):

            while heap and heap[0][0] <= w:
                c,p = heappop(heap)
                heappush(heap2,-p)
            if not heap2:
                break
            w -= heappop(heap2)
        return w