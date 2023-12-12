class Solution:
    def reverseWords(self, s: str) -> str:
        word_lists=s.split()
        return " ".join(word_lists[::-1])