# class Trie:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
    
#     def insert(self,word):
#         curr = self
        
#         for char in word:
#             idx = ord(char) - ord('a')
            
#             if char not in curr.children[idx]:
#                 curr.children[idx] = Trie()
#             curr = children[idx]
            
#     def search(self,word):
       

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key=len)
        
        max_len = 0
        longest_word = ""
        good_words = set()
        
        for word in words:
            if len(word) == 1:
                good_words.add(word)
                
            elif word[:-1] in good_words:
                good_words.add(word)
                
            if word in good_words:
                if max_len < len(word):
                    max_len = len(word)
                    longest_word = word
                    
                elif max_len == len(word):
                    longest_word = min(word,longest_word)
        
        return longest_word
            
                