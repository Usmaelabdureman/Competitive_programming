class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            ans=[]
            for char in s:
                if char != "#":
                    ans.append(char)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
            