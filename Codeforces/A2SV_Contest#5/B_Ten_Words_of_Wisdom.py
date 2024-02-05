"""
In the game show "Ten Words of Wisdom", there are n
 participants numbered from 1
 to n
, each of whom submits one response. The i
-th response is ai
 words long and has quality bi
. No two responses have the same quality, and at least one response has length at most 10
.

The winner of the show is the response which has the highest quality out of all responses that are not longer than 10
 words. Which response is the winner?

Input
The first line contains a single integer t
 (1≤t≤100
) — the number of test cases.

The first line of each test case contains a single integer n
 (1≤n≤50
) — the number of responses.

Then n
 lines follow, the i
-th of which contains two integers ai
 and bi
 (1≤ai,bi≤50
) — the number of words and the quality of the i
-th response, respectively.

Additional constraints on the input: in each test case, at least one value of i
 satisfies ai≤10
, and all values of bi
 are distinct.

Output
For each test case, output a single line containing one integer x
 (1≤x≤n
) — the winner of the show, according to the rules given in the statement.

It can be shown that, according to the constraints in the statement, exactly one winner exists for each test case.

Example
inputCopy
3
5
7 2
12 5
9 3
9 4
10 1
3
1 2
3 4
5 6
1
1 43
outputCopy
4
3
1
Note
In the first test case, the responses provided are as follows:

Response 1: 7
 words, quality 2
Response 2: 12
 words, quality 5
Response 3: 9
 words, quality 3
Response 4: 9
 words, quality 4
Response 5: 10
 words, quality 1
We can see that the responses with indices 1
, 3
, 4
, and 5
 have lengths not exceeding 10
 words. Out of these responses, the winner is the one with the highest quality.

Comparing the qualities, we find that:

Response 1 has quality 2
.
Response 3 has quality 3
.
Response 4 has quality 4
.
Response 5 has quality 1
.
Among these responses, Response 4 has the highest quality.

"""# Read the number of test cases

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