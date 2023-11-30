class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)
        ans = 0
        for num in nums:
            freq[num] += 1
        for count in freq.values():
            ans += count * (count - 1) // 2
        return ans
            
            
       
       
        