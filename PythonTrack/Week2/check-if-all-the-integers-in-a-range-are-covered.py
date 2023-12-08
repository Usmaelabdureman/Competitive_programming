class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        combined_ranges = []
        for start, end in ranges:
            combined_ranges.extend(range(start, end + 1))
        #I used set for faster membership checking
        # print(combined_ranges)
        combined_ranges = set(combined_ranges)
        for i in range(left, right + 1):
            if i not in combined_ranges:
                return False
        return True