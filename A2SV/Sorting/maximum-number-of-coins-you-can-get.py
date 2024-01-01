class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles,reverse=True)[1:len(piles)*2//3:2])
    #     piles.sort()
    #     res = 0

    #     for i in range(len(piles) // 3, len(piles), 2):
    #         res += piles[i]
        
    #     return res