# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # for i in range(n):
        #     if isBadVersion(i):
        #         return i
        # return n


        low = 0
        high = n

        while high - low > 1 :
            mid = low + (high - low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid

        return high
