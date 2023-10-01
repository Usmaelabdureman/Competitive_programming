import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26  # Since there are 26 possible uppercase English letters
        
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        max_heap = []
        for count in task_counts:
            if count > 0:
                heapq.heappush(max_heap, -count)  # Use negative count for max heap
        
        time = 0
        
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap))
            
            for item in temp:
                if item < -1:
                    heapq.heappush(max_heap, item + 1)
            
            if not max_heap:
                time += len(temp)
            else:
                time += n + 1
        
        return time
