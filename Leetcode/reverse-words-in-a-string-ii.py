"""
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

 

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]
 

Constraints:

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
    """

from typing import List
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        
        def swap(start, end, slist):
            while start < end:
                slist[start], slist[end] = slist[end], slist[start]
                start += 1
                end -= 1
        left =0
        for right in range(len(s)):
            if s[right] == " ":
                swap(left, right-1, s)
                left = right+1
        swap(left, len(s)-1, s)
if __name__ == '__main__':
    test_case_1 = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    test_case_2 = ["a"]
    solution = Solution()
    solution.reverseWords(test_case_1)
    solution.reverseWords(test_case_2)
    print(test_case_1)
    print(test_case_2)
    
 