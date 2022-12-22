class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr=set()
        left_ptr=0
        res=0
        for right_ptr in range (len(s)):
            while s[right_ptr] in substr:
                substr.remove(s[left_ptr])
                left_ptr+=1
            substr.add(s[right_ptr])
            res=max(res,right_ptr-left_ptr+1)
        return res