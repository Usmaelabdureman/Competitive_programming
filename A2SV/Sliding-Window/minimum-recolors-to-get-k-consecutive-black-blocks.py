class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_white = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                min_white += 1

        left = 0
        right = k
        res = min_white
        while right < len(blocks):
            if blocks[left] == 'W':
                min_white -= 1
            if blocks[right] == 'W':
                min_white += 1
            res = min(min_white, res)
            left += 1
            right += 1

        return res
