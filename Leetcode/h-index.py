class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        len_arr=len(citations)
        for i in range(len_arr):
            if len_arr-i<=citations[i]:
                return len_arr-i
        return 0