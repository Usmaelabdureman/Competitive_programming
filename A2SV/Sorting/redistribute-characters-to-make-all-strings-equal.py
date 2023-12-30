class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count=Counter(char for word in words for char in word)
        for val in count.values():
            if val % len(words) != 0:
                return False
        
        return True
        