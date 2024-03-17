class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = []
        for card in reversed(deck):
            if ans:
                ans.insert(0, ans.pop())
            ans.insert(0, card)
        return ans
