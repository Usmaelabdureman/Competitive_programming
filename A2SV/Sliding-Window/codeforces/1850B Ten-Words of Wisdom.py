
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the number of responses
    n = int(input())

    # Initialize variables to track the winner
    max_quality = 0
    winner = 0

    # Iterate over each response
    for i in range(1, n+1):
        # Read the number of words and quality of the response
        words, quality = map(int, input().split())

        # Check if the number of words is not greater than 10
        if words <= 10:
            # Check if the quality is greater than the current maximum quality
            if quality > max_quality:
                max_quality = quality
                winner = i

    # Print the winner for the current test case
    print(winner)
