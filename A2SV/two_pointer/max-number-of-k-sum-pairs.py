class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        # for i in range(n):
        #     min_index=i
        #     for j in range(i+1,n):
        #         if nums[j]<nums[min_index]:
        #             min_index=j
        #     nums[min_index],nums[i] = nums[i], nums[min_index]
        left =0
        right = len(nums)-1
        cnt=0
        while left<right:
            if nums[left]+nums[right] >k:
                right-=1
            elif nums[left]+nums[right] < k:
                left+=1
            else:
                left+=1
                right-=1
                cnt+=1
        return cnt
