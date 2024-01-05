class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount={}
        sCount={}
        if len(p)>len(s):return []
        for i in range(len(p)):
            pCount[p[i]]=1+pCount.get(p[i],0)
            sCount[s[i]]=1+sCount.get(s[i],0)
        res=[0] if pCount==sCount else []
        left=0
        for right in range(len(p),len(s)):
            sCount[s[right]]=1+sCount.get(s[right],0)
            sCount[s[left]]-=1
            if sCount[s[left]]==0:
                sCount.pop(s[left])
            left+=1
            if sCount==pCount:
                res.append(left)
           
        return res
            