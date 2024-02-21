class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map_index={}
        for i,char in enumerate(s):
            map_index[char]=i


        start =0
        end = 0
        ans=[]
        for idx , char in enumerate(s):
            end=max(end,map_index[char])
            if idx==end:
                ans.append(idx-start+1)
                start=idx+1
        return ans   