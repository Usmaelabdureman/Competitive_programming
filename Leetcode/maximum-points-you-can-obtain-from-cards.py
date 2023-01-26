class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N, left, right = len(cardPoints), 0, len(cardPoints) - k
        currentMax = sum(cardPoints[right:])
        maxPoint = currentMax
        for _ in range(k):
            currentMax += cardPoints[left] - cardPoints[right]
            maxPoint = max(maxPoint, currentMax)
            left += 1
            right += 1
        return maxPoint
        
