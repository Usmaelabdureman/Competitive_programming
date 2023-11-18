class Solution:
    def reverseWords(self, s: str) -> str: 
        s.strip()
        words=s.split()
        left=0
        right =len(words)-1
        while left < right:
            words[left],words[right] = words[right],words[left]
            left+=1
            right-=1
        return " ".join(words)