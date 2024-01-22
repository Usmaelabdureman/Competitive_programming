class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        counter = Counter(nums)
        for k,v in counter.items():
            if v > 1 :
                ans.append(k)
        for i in range(1,n+1):
            if i not in nums:
                ans.append(i)
        return ans