class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) < 2: return ""
        
        char_dict = set(list(s))

        for i,c in enumerate(s):
            
            if c.upper() in char_dict and c.lower() in char_dict: 
                continue
            
            first = self.longestNiceSubstring(s[:i])
            second = self.longestNiceSubstring(s[i+1:])
            
            return max(first, second, key = len)
        
        return s