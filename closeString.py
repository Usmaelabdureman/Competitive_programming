class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word2)!=len(word1):return False
        if sorted(word1)==sorted(word2):return True
        dict1={}
        dict2={}
        for ch in word1:
            if ch not in word2:
                return False
        for i in word1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in word2:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
        return sorted(dict1.values())==sorted(dict2.values()) 