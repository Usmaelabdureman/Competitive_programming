from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return [num for num, c in count.items() if c > 1]
