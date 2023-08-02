class Solution:
    def valid(self, s, start, length):
        return length == 1 or (
            s[start] != '0' and (length < 3 or s[start:start + length] <= "255")
        )

    def helper(self, s, startIndex, dots, ans):
        remainingLength = len(s) - startIndex
        remainingNumberOfIntegers = 4 - len(dots)
        if (
            remainingLength > remainingNumberOfIntegers * 3
            or remainingLength < remainingNumberOfIntegers
        ):
            return
        if len(dots) == 3:
            if self.valid(s, startIndex, remainingLength):
                sb = []
                last = 0
                for dot in dots:
                    sb.append(s[last : last + dot])
                    last += dot
                    sb.append(".")
                sb.append(s[startIndex:])
                ans.append("".join(sb))
            return
        for curPos in range(1, 4):
            if curPos <= remainingLength:
                # Append a dot at the current position.
                dots.append(curPos)
                # Try making all combinations with the remaining string.
                if self.valid(s, startIndex, curPos):
                    self.helper(s, startIndex + curPos, dots, ans)
                # Backtrack, i.e. remove the dot to try placing it at the next position.
                dots.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.helper(s, 0, [], ans)
        return ans

    