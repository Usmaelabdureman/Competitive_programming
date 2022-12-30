class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        arr_len = len(changed)
        ans = []
        if (arr_len % 2 != 0):
            return []
        count = Counter(changed)
        for i in changed:
            if i == 0 and count[i] >= 2:
                count[i] -= 2
                ans.append(i)
            elif i > 0 and count[i] and count[i*2]:
                count[i] -= 1
                count[i*2] -= 1
                ans.append(i)
        
        return ans if len(ans) == (len(changed) // 2) else []
      
        