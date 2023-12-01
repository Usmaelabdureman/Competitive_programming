class Solution:
    def romanToInt(self, s: str) -> int:
        rom2Int={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        answer=0
        for i in range(len(s)):
            if i+1<len(s) and rom2Int[s[i]]<rom2Int[s[i+1]]:
                answer-=rom2Int[s[i]]
            else:
                answer += rom2Int[s[i]]
        return answer