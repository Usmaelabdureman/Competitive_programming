class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        lenghtOfarray = len(piles)
        count = 0
        res = 0
        for i in range(lenghtOfarray):
            res += piles[-2-(i*2)]
            count += 1
            if count == lenghtOfarray // 3:
                break
            else: 
                continue
        return res