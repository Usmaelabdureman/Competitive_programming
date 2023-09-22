class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)
        for char in strs:
            count=[0]*26
            for et in char:
                count[ord(et)-ord("a")]+=1
            res[tuple(count)].append(char)
        return res.values()
        