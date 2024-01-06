class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left, right = 0, 0
        while right < len(typed):
            if left < len(name) and name[left] == typed[right]:
                left += 1
                right += 1
            elif right > 0 and typed[right] == typed[right - 1]:
                right += 1
            else:
                return False
        return left == len(name)