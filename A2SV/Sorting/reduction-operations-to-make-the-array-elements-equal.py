class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        opt=0
        cnt=0
        for i in range(1, len(nums)):
            if nums[i-1]!=nums[i]:
                cnt+=1
            opt+=cnt
        return opt