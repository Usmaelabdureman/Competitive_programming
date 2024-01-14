class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        count = 0
        time = intervals[0][1]
        for s, e in intervals[1:]:
            if s >= time:
                time = e
            else:
                count += 1
        return count

