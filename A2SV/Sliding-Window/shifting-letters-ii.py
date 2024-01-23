class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_amount = [0] * (n + 1)
        total_shift = 0
        result = []

        for shift in shifts:
            l, r, direction = shift
            if direction == 0:
                shift_amount[l] -= 1
                shift_amount[r + 1] += 1
            else:
                shift_amount[l] += 1
                shift_amount[r + 1] -= 1

        for i in range(n):
            total_shift += shift_amount[i]
            k = total_shift % 26
            p = (ord(s[i]) - ord('a') + k + 26) % 26
            result.append(chr(ord('a') + p))

        return ''.join(result)