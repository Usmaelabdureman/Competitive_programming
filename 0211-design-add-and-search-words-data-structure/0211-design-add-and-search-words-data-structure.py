class TrieNode:
    def __init__(self):
        self.children = {}  # dictionary mapping characters to child nodes
        self.is_word = False  # indicates if the node represents the end of a word
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # the root of the trie
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        
    def search(self, word: str) -> bool:
        
        def search_helper(node, i):
            if i == len(word):
                return node.is_word
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if search_helper(child, i+1):
                        return True
            else:
                child = node.children.get(char)
                if child:
                    return search_helper(child, i+1)
            return False
            
        return search_helper(self.root, 0)
