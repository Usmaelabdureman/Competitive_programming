class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=[set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm')]
        ans=[]    
        for word in words:
            if any(set(word.lower()) <= row for row in rows):
                ans.append(word)
        return ans
                
