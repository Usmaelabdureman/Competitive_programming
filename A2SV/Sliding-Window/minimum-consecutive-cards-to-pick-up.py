class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        last_index = {}
        ans = float('inf')
        for i in range(n):
            if cards[i] in last_index:
                ans = min(ans, i - last_index[cards[i]] + 1)
            last_index[cards[i]] = i
        return ans if ans != float('inf') else -1
