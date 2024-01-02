class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_merged=[]
        for char in s:
            if not char.isalnum():
                continue
            else:
                s_merged.append(char.lower())
                
        left =0
        right =len(s_merged)-1
        while left<=right:
            if s_merged[left] == s_merged[right]:
               left+=1
               right-=1
            else:
                return False
        return True

        