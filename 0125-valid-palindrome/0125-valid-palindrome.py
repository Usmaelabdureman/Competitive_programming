class Solution:
    def isPalindrome(self, s: str) -> bool:
        word= ("".join(filter(str.isalnum, s))).lower()
        return word == word[::-1]
            
        