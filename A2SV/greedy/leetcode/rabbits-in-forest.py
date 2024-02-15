class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        ans = 0
        
        for ans_count in answers:
            if ans_count not in count:
                count[ans_count] = 0
            count[ans_count] += 1
            
            if count[ans_count] == ans_count + 1:
                ans += ans_count + 1
                count.pop(ans_count)
        
        for ans_count in count:
            ans += ans_count + 1
        
        return ans