class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # set_num = set(nums)
        # n = len(nums)
        
        # for i in range(1,n+1):
        #     if i not in set_num:
        #         return i
        # return n+1



        #  method two using cycle Sort 
        n = len(nums)
        i = 0
        
        while i < n:
            cor_pos = nums[i] - 1
            if nums[i] > n or nums[i] <= 0:
                i += 1
                continue

            if cor_pos != i and cor_pos < n and nums[cor_pos] != nums[i]:
                nums[i] , nums[cor_pos] = nums[cor_pos],nums[i]
                
            else:
                i += 1
        # print(nums)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1