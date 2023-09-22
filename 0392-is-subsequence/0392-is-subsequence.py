class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for both strings
        s_pointer, t_pointer = 0, 0
        
        # Iterate through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If the current characters match, move the s_pointer
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Always move the t_pointer
            t_pointer += 1
        
        # If s_pointer reached the end of s, it means all characters of s are found in t in order.
        return s_pointer == len(s)
