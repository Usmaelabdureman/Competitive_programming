class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # step 1 map to store last index of each character in the string
        map_index={}
        for i,char in enumerate(s):
            map_index[char]=i

        # step 2 Iterate through the string. For each character:

        # Update the value of "end" to be the maximum of its current value and the last index of the character in the map.
        start =0
        end = 0
        ans=[]
        for idx , char in enumerate(s):
            end=max(end,map_index[char])
            if idx==end:
                ans.append(idx-start+1)
                start=idx+1
        return ans   