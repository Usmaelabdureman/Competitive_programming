from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        max_freq = max(freq.values())
        max_freq_elts = [key for key, value in freq.items() if value == max_freq]
        
        ans = sum([freq[elt] for elt in max_freq_elts])
        
        return ans
