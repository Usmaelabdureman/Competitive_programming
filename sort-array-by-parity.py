from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd
      
# Time complexity: O(n)
# Space complexity: O(n)
test=Solution()
print(test.sortArrayByParity([3,1,2,4]))