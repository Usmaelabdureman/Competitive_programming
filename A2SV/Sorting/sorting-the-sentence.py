class Solution:
    def sortSentence(self, s: str) -> str:
        words = {}
        for word in s.split():
            words[word[-1]] = word[:-1]
        lst=[]
        for i in sorted(words):
            lst.append(words[i])
        return " ".join(lst)
            