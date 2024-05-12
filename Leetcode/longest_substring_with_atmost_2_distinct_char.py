"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
Algorithm
Use HashMap to do it, HashMap records the number of occurrences of each character,

Then if the number of mappings in HashMap exceeds two, one mapping needs to be deleted here.
    """
from collections import Counter
class Solution:
     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
         cnt = Counter()
         ans=0
         left=0
         for right,c in enumerate(s):
             cnt[c]+=1
             while len(cnt)>2:
                 cnt[s[left]]-=1
                 if cnt[s[left]]==0:
                     del cnt[s[left]]
                 left+=1
             ans=max(ans,right-left+1)
         return ans
         