"""
You are given a 0-indexed string s consisting of only lowercase English letters. Return the number of substrings in s that begin and end with the same character.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "abcba"
Output: 7
Explanation:
The substrings of length 1 that start and end with the same letter are: "a", "b", "c", "b", and "a".
The substring of length 3 that starts and ends with the same letter is: "bcb".
The substring of length 5 that starts and ends with the same letter is: "abcba".
Example 2:

Input: s = "abacad"
Output: 9
Explanation:
The substrings of length 1 that start and end with the same letter are: "a", "b", "a", "c", "a", and "d".
The substrings of length 3 that start and end with the same letter are: "aba" and "aca".
The substring of length 5 that starts and ends with the same letter is: "abaca".
Example 3:

Input: s = "a"
Output: 1
Explanation:
The substring of length 1 that starts and ends with the same letter is: "a".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
"""
# def checkEquality(s):
#     return (ord(s[0])== ord(s[len(s)-1]))
# def  SubstringWithEqualEnds(s):
#     result =0

#     for i in range(len(s)):
#         for j in range(1,len(s)-i+1):
#             if checkEquality(s[i:i+j]):
#                 result+=1
#     return result

from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt =Counter()
        ans =0
        for c in s:
            cnt[c]+=1
            ans+=cnt[c]
        return ans

test1="abcab"
print(Solution().numberOfSubstrings(test1))

s = "abacad"
print(Solution().numberOfSubstrings(s))