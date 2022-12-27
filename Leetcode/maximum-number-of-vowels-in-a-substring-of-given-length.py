class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','o','u','i'}
        len_arr=len(s)
        cnt=0
        for i in range(k):
            if s[i] in vowels:cnt+=1
        #initializing starting index and end index for windows

        left=0
        right=k-1
        max_vowel = cnt
        while (right < len_arr-1):
            if s[left] in vowels: #if vowels already counted in previous window remove it from current window
                cnt-=1
            left+=1
            right+=1
            if s[right] in vowels:
                cnt+=1
            max_vowel=max(max_vowel,cnt)
        return max_vowel

            