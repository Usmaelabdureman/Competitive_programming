class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_cards = {front for front,back in zip(fronts,backs) if front == back}
        combined_card=fronts+backs
        return min([num for num in combined_card if num not in same_cards] or [0])
