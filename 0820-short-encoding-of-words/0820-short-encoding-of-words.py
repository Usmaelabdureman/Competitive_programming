# class TrieNode:
#     # Trie node class
#     def __init__(self):
#         self.children = [None for _ in range(26)]
#         self.is_end = False
        
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def insert(self,word):
#         curr = self.root
#         for char in word:
#             idx = ord(char) - ord('a')
#             if not curr.children[idx]:
#                 curr.children[idx] = TrieNode()
#         curr = curr.children[idx]
#         is_end = True

# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
        
#         rev_words = [  w[::-1]  for w in words]
        
        
#         trie = Trie()
#         for word in rev_words:
#             trie.insert(word)
        
#         def findLen(word,length):
#             isLeaf = True
#             curLen = 0
            
#             for i in range(26):
#                 if word.children[i] is not None:
#                     isLeaf = False
#                     findLen(word.children[i],length+1)
#                 if isLeaf:
#                     curLen += length
#             return curLen
        
#         return findLen(trie,1)

class Solution(object):
    def minimumLengthEncoding(self, words):
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)
        
                
            
            
        
        
        
        