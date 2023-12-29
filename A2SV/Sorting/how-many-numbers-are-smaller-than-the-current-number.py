class Solution(object):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_arr=sorted(nums)
        mydict={}
        res=[]
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in mydict:
                mydict[sorted_arr[i]]=i
        for i in nums:
            if i in mydict:
                res.append(mydict[i])
        return res