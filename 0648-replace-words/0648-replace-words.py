class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.ref = -1   #Reference index to keep track of the word's index from the dictionary in the trie.


    def insert(self, w: str, i: int):
        
        node = self
        
        for char in w:
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.ref = i

    def search(self, w: str) -> int:
        node = self
        
        for char in w:
            
            idx = ord(char) - ord("a")
            
            if not node.children[idx]:
                return -1
            node = node.children[idx]
            if node.ref != -1:
                return node.ref
        return -1


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        # Insert all words from the dictionary into the trie with their indx
        
        for idx, word in enumerate(dictionary):
            trie.insert(word, idx)
            
        res = []
        
        # Split the sentence into words and replace them accordingly
        for w in sentence.split():
            idx = trie.search(w)
            res.append(dictionary[idx] if idx != -1 else w)
            
        return " ".join(res)
