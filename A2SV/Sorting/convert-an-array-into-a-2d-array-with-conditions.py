class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        ans=[]
        for key,value in freq.items():
            for i in range(value):
                if len(ans)<=i:
                    ans.append([])
                ans[i].append(key)
        return ans
        