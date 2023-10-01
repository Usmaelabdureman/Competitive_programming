class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        for i in nums:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        res=sorted(mydict.items(),key=lambda value:value[1],reverse=True)
        return [res[i][0] for i in range(k)]