
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        
        for num in nums:
            if num % 2 == 0:
                freq[num] += 1
        
        most_freq = -1
        max_freq = 0
        
        for num, frequency in freq.items():
            if frequency > max_freq or (frequency == max_freq and num < most_freq):
                most_freq = num
                max_freq = frequency
                
        return most_freq
