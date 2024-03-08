class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substr=set()
        seen={}
        left_ptr=0
        res=0
        start=0
        # for right_ptr in range (len(s)):
        #     while s[right_ptr] in substr:
        #         substr.remove(s[left_ptr])
        #         left_ptr+=1
        #     substr.add(s[right_ptr])
        #     res=max(res,right_ptr-left_ptr+1)
        for end in range(len(s)):
            curr_char=s[end]
            if curr_char in seen and seen[curr_char]>=start:
                start=seen[curr_char]+1
            seen[curr_char]=end
            res = max(res,end-start+1)
        return res

            