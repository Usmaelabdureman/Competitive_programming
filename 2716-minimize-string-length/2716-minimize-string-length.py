class Solution:
    def minimizedStringLength(self, s: str) -> int:
        distinct_string = set(s)
        return len(distinct_string)
        