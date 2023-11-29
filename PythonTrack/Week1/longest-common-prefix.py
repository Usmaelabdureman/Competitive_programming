class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Sort the strings to easily find the common prefix
        strs.sort()
        
        # Compare the first and last string in the sorted array
        first = strs[0]
        last = strs[-1]
        prefix = ""
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix += first[i]
            else:
                break
        
        return prefix

            