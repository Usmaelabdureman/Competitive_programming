class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        ans = [0] * len(code)
        
        if k == 0:
            return ans
        
        for i in range(len(ans)):
            
            if k > 0:
                for j in range(i+1,i+k+1):
                    ans[i] += code[j%len(code)]
            else:
                for j in range(i-abs(k),i):
                    ans[i] += code[(j + len(code))%len(code)]
                    
        return ans
            