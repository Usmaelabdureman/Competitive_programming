class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        lst=[]
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                if nums[i]==nums[j]:
                    lst.append(zip(str(i),str(j)))
        return len(lst)