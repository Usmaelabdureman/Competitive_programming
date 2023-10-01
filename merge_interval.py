class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e:e[0]) #sort intervals by first element. Its time complexity is O(NlogN)
        output=[intervals[0]]             # Space complexity : O(log⁡N)
        for start,end in intervals[1:]:
            lastEnd=output[-1][1] #last element of previous interval 
            if start<=lastEnd:
                output[-1][1]=max(lastEnd,end)
            else:
                output.append([start,end])
        return output

    