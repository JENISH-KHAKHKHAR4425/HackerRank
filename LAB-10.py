# Matrix Chain Multiplication using Dynamic Programming

import sys

def matrixChainOrder(p, n):
    # Step 1: Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # dp[i][j] = minimum number of multiplications
    # needed to compute the matrix A[i]...A[j]

    # Step 2: l is chain length
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n-1]


# Driver Code
if __name__ == "__main__":
    # Example: dimensions of matrices A1(10x30), A2(30x5), A3(5x60)
    arr = [10, 30, 5, 60]   # dimensions array
    n = len(arr)

    min_cost = matrixChainOrder(arr, n)
    print("Minimum number of multiplications is:", min_cost)
