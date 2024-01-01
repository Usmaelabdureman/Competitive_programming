class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        maxTime=0
        n=len(processorTime)
        for i in range(n):
            maxTime=max(maxTime,processorTime[i]+tasks[4*n-1-4*i])
        return maxTime