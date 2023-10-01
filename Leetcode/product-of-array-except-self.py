class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[0]*len(nums)
        res[0]=1
        for i in range(1,len(nums)):
            res[i]=nums[i-1]*res[i-1]
        sufProd=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*sufProd
            sufProd=sufProd*nums[i]
        return res
            