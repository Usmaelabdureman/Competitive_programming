class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter=Counter(nums)
        ans=0
        for value in counter.values():
            if value == 1:
                return -1
            ans+=ceil(value/3)

        return ans