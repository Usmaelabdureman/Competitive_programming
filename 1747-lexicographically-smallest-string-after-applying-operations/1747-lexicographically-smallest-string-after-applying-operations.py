class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        vis = [False] * n
        res = s
        # double the length of s for convenience in extracting the rotated string t
        s = s + s
        i = 0
        while not vis[i]:
            vis[i] = True
            for j in range(10):
                k_limit = 0 if b % 2 == 0 else 9
                for k in range(k_limit + 1):
                    # before each accumulation, re-truncate t
                    t = list(s[i : i + n])
                    for p in range(1, n, 2):
                        t[p] = str((int(t[p]) + j * a) % 10)
                    for p in range(0, n, 2):
                        t[p] = str((int(t[p]) + k * a) % 10)
                    t_str = "".join(t)
                    if t_str < res:
                        res = t_str
            i = (i + b) % n
        return res