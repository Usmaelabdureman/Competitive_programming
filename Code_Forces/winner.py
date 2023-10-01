scores = {}  # dictionary to store the scores of each player
num_rounds=int(input())
# play the game and update scores after each round
for i in range(num_rounds):
    name, points = input().split()  # read the name and points for this round
    points = int(points)
    scores[name] = scores.get(name, 0) + points  # update the score for this player

# find the maximum score achieved by any player
max_score = max(scores.values())

# find the first player who achieved the maximum score
winner = None
for name, score in scores.items():
    if score == max_score:
        if winner is None or winner[1] > score:
            winner = (name, score)
            # print(winner)
print(winner[0])  # print the name of the winner
