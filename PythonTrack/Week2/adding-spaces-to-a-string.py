class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        j = 0  # Index tracker for spaces
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(s[i])
        # If there are spaces left after the string ends
        while j < len(spaces):
            result.append(' ')
            j += 1
        return ''.join(result)
