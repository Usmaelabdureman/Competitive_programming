class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''.join(char for char in s if char.isalnum())
        st=st.lower()
        return st==st[::-1]