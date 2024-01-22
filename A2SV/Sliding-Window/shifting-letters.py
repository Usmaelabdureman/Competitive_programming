class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts.reverse()
        sh = list(accumulate(shifts))
        sh.reverse()
        ans = []
        for i, ch in enumerate(s):
            ans.append(chr((ord(ch) - ord('a') + sh[i]) % 26 + ord('a')))
        return ''.join(ans)