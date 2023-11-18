"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
    """

class Solution:
    def reverseWords(self, s: str) -> str:
        def swap(start, end, slist):
            while start < end:
                slist[start], slist[end] = slist[end], slist[start]
                start += 1
                end -= 1
        # use two pointer to find the start and end of each word
        wstart, wend = 0, 0
        slist = list(s)
        for i in range(0, len(slist)):
            if slist[i] == " ":
                wend = i - 1
                swap(wstart, wend, slist)
                wstart = i + 1
            elif i + 1 == len(slist):
                swap(wstart, i, slist)
                
        return "".join(slist)
        
        
        
        
                