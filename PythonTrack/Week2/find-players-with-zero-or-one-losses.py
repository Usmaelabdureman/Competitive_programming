class Solution:
    def findWinners(self, matches):
        winner = defaultdict(int)
        loser = defaultdict(int)

        for win, loss in matches:
            winner[win] += 1
            loser[loss] += 1
        
        winners = [player for player in winner if winner[player] > 0 and loser[player] == 0]
        one_time_losers = [player for player in loser if loser[player] == 1]

        return [sorted(winners), sorted(one_time_losers)]
