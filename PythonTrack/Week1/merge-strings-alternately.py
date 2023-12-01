class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        word1_ptr=0
        word2_ptr=0
        while word1_ptr<len(word1) and word2_ptr <len(word2):
            merged+= word1[word1_ptr]
            merged+=word2[word2_ptr]
            word1_ptr+=1
            word2_ptr+=1
        if word1_ptr==len(word1) and word1_ptr< len(word2):
            merged+=word2[word2_ptr:]
        if word2_ptr==len(word2) and word2_ptr< len(word1):
            merged+=word1[word1_ptr:]
        return merged