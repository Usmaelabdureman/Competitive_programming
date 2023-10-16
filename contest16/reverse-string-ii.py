"""
Reverse Words in a String II
Given an input string, reverse the string word by word.
Example:
Input:  
["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
​
Output: 
["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do itin-placewithout allocating extra space?
Topics: Two Pointers, String
"""
from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        # reverse the whole string
        def reverse (s,start,end):
            while start < end:
                s[start],s[end] = s[end],s[start]
                start += 1
                end -= 1
        reverse(s,0,len(s)-1)
        # reverse each word
        start = 0
        end = 0
        while end < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            reverse(s,start,end-1)
            start = end + 1
            end += 1

if __name__ == "__main__":
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    # print(Solution().reverseWords(s))
    Solution().reverseWords(s)
    print(s)
