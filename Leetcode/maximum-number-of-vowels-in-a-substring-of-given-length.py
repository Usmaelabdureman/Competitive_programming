class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','o','u','i'}
        cnt=0
        left,right=0,0
        max_count = 0
        while left <= len(s) - k and right < len(s):
            if (right - left + 1) < k:
                if s[right] in vowels:
                    cnt += 1
                right += 1
            elif (right - left + 1) == k:
                print(left, right)
                if s[left] in vowels:
                    cnt -= 1
                if (right+1) < len(s) and s[right+1] in vowels:
                    cnt += 1
                if cnt > max_count:
                    max_count = cnt
                left += 1
            right += 1

        return max_count