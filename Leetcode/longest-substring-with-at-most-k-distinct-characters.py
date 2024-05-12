from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = Counter()
        ans=0
        left=0
        for right,c in enumerate(s):
            cnt[c]+=1
            while len(cnt)>k:
                cnt[s[left]]-=1
                if cnt[s[left]]==0:
                    del cnt[s[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
    
if __name__=="__main__":
    test_case_1= "eceba"
    k=2
    print(Solution().lengthOfLongestSubstringKDistinct(test_case_1,k))