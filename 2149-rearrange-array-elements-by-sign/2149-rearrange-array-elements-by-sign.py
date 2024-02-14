class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums=[num for num in nums if num>0]
        negative_nums=[num for num in nums if num<0]
        ans=[]
        for i in range(len(positive_nums)):
            ans.append(positive_nums[i])
            ans.append(negative_nums[i])
        return ans
        