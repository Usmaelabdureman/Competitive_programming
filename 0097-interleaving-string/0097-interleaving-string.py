class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        
        if len_s1 + len_s2 != len_s3:
            return False
        
        # Create a 2D DP array to store whether the interleaving of s1 and s2 up to certain lengths can form s3.
        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        
        # Base case: both strings are empty, so s3 is also empty.
        dp[0][0] = True
        
        # Initialize the first row, which represents interleaving s1 with an empty string s2.
        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Initialize the first column, which represents interleaving s2 with an empty string s1.
        for j in range(1, len_s2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill in the DP table based on the interleaving logic.
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len_s1][len_s2]
