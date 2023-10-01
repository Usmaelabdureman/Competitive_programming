class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0 and x<=(2**31)-1:
            x=str(x) 
            return x==x[::-1]
        return False