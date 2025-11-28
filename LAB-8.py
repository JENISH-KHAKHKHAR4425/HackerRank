# Longest Common Subsequence using Dynamic Programming

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Step 1: Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Reconstruct the LCS string
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_str))


# Driver Code
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"

    length, sequence = lcs(X, Y)
    print("Length of LCS:", length)
    print("LCS:", sequence)
