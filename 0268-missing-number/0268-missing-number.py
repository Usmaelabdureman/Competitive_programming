class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return list(set(range(0,len(nums)+1)) - set(nums))[0]

        n = len(nums)
        i = 0

        while i < n:
            cor_pos = nums[i]

            if cor_pos < n and nums[i] != nums[cor_pos]:

                nums[i], nums[cor_pos] = nums[cor_pos], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i


        return n
