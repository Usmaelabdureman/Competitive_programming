class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        char_count = {}
    
        # Count characters in the first word
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterate through the remaining words to update character frequencies
        for word in words[1:]:
            temp_count = {}
            for char in word:
                if char in char_count and char_count[char] > 0:
                    temp_count[char] = temp_count.get(char, 0) + 1
                    char_count[char] -= 1
            
            # Update char_count with temp_count
            char_count = temp_count
        
        # Create the result list based on char_count
        result = []
        for char, count in char_count.items():
            result.extend([char] * count)
        
        return result