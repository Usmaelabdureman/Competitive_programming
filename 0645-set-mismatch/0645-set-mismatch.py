class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # ans = []
        # counter = Counter(nums)
        # for k,v in counter.items():
        #     if v > 1 :
        #         ans.append(k)
        # for i in range(1,n+1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans
        i = 0
        while i < n:
            corr_pos = nums[i] - 1
            
            if corr_pos != i and  nums[i] != nums[corr_pos]:
                nums[corr_pos],nums[i] = nums[i],nums[corr_pos]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]

        return []