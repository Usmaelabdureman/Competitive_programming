class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, w):
        
        curr  = self
        
        for c in w:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Trie()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, w):
        
        curr = self
        
        for c in w:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.is_end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(s):
            return not s or any(trie.search(s[:i]) and dfs(s[i:]) for i in range(1, len(s) + 1))

        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        return dfs(s)