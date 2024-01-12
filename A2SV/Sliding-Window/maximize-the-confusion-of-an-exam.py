class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left=0
        n=len(answerKey)
        count={'T':0,'F':0}
        max_count=0
        max_cons=0
        for right in range(n):
            count[answerKey[right]]+=1

            max_count=max(max_count,count['T'],count['F'])

            while (right-left+1-max_count) > k:
                count[answerKey[left]]-=1
                left+=1
            max_cons=max(max_cons,right-left+1)
        return max_cons