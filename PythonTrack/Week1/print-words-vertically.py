class Solution:
    def printVertically(self, s: str) -> List[str]:
        ss=s.split()
        max_len=max(len(w) for w in ss)
        cols=['']*max_len 
        for word in ss:
            word+=' '*(max_len -len(word)) #add pad with spaces to the word if the length of the word is short.
            for index,char in enumerate(word):
                cols[index]+=char # 
        return [col.rstrip() for col in cols]