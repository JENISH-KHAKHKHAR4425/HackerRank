# 0/1 Knapsack Problem using Dynamic Programming

def knapSack(W, wt, val, n):
    # Step 1: Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 2: Build table in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Step 3: Find selected items
    res = dp[n][W]
    w = W
    selected_items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected_items.append(i - 1)  # Store item index
            res -= val[i - 1]
            w -= wt[i - 1]

    return dp[n][W], selected_items


# Driver Code
if __name__ == "__main__":
    val = [60, 100, 120]   # values (profits)
    wt = [10, 20, 30]      # weights
    W = 50                 # capacity of knapsack
    n = len(val)

    max_value, items = knapSack(W, wt, val, n)
    print("Maximum Value in Knapsack:", max_value)
    print("Selected Item Indices:", items)
