class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        freq = defaultdict(int)
        res = []
        
        for num in nums:
            freq[num] += 1
            
            if freq[num] == 2:
                res.append(num)
        return res