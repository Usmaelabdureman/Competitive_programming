t = int(input())
 
for _ in range(t):
    n = int(input())
    S = list(range(1, n+1))

    # perform n-1 operations
    for i in range(n-1):
        # find the largest and smallest numbers in S
        print(S)
        Smax = max(S)
        Smin = min(S)
        # remove Smax and Smin from S and add Smax-Smin to S
        S.remove(Smax)
        S.remove(Smin)
        S.append(Smax-Smin)
    # the final number in S is the answer
    print(S[0])