class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # method one using the concatination of the string
        word1Combined="".join(word1)
        word2Combined="".join(word2)
        return word1Combined == word2Combined

        # method two using two pointer Space Complexity: O(1) Time Complexity:O(n*m)
        ptr1 = ptr2 = char1 = char2 = 0
        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1][char1] != word2[ptr2][char2]:
                return False
            
            char1 += 1
            char2 += 1
            
            # Move to the next word in the arrays
            if char1 >= len(word1[ptr1]):
                char1 = 0
                ptr1 += 1
            
            if char2 >= len(word2[ptr2]):
                char2 = 0
                ptr2 += 1
        
        # Ensure both pointers are at the end of their respective arrays
        return ptr1 == len(word1) and ptr2 == len(word2)
