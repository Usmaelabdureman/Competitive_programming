class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        temp={k:v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}  
        return ''.join([key * val for key, val in temp.items()])