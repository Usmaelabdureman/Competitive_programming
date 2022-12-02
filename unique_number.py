class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums=[str(c) for c in arr]
        mydict={}
        freq=[]
        for i in nums:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        for i in mydict.values():
            if i not in freq:
                freq.append(i)
            else :
                return False
        return True