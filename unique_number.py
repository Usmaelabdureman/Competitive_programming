class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums=[str(c) for c in arr]
        myDict={}
        freq=[]
        for i in nums:
            if i in myDict:
                myDict[i]+=1
            else:
                myDict[i]=1
        for i in myDict.values():
            if i not in freq:
                freq.append(i)
            else :
                return False
        return True