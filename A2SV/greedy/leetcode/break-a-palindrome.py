class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        n = len(palindrome)
        
        if len(palindrome) == 1: return ""

    
        left = 0
        right = len(palindrome) - 1

        while left < right:
            if palindrome[left] == 'a':
                left +=1
                right -= 1

            else:
                palindrome[left] = 'a'
                break
        else:
            palindrome[-1] = 'b'
            
        return ''.join(palindrome)