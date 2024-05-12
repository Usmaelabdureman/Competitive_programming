from bisect import insort
class MedianFinder:
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        insort(self.heap, num)
       
    def findMedian(self) -> float:
        n = len(self.heap)
        return sorted_[n//2] if n%2 else (sorted_[n//2] + sorted_[n//2-1])/2
