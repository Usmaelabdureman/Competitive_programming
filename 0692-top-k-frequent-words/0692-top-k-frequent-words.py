class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        
        freq_dict = defaultdict(int)
        
        for word in words:
            freq_dict[word] += 1
            
        buckets = [[] for _ in range(n + 1)]
        
        for word , freq in freq_dict.items():
            buckets[freq].append(word)
        
        ans  = []
        
        for bucket in reversed(buckets):
            bucket.sort()
            ans.extend(bucket)
            if len(ans) >= k:
                break
        return ans[:k]