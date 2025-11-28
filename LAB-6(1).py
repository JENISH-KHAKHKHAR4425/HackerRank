# 0/1 Knapsack using Greedy Approach
def knapsack_01_greedy(values, weights, capacity):
    n = len(values)
    
    # Calculate value-to-weight ratio
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    # Sort by ratio (descending order)
    ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    chosen_items = []
    
    for r, v, w in ratio:
        if w <= capacity:
            chosen_items.append((v, w))
            total_value += v
            capacity -= w
    
    return total_value, chosen_items


# Example Run
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    
    max_value, items = knapsack_01_greedy(values, weights, capacity)
    
    print("0/1 Knapsack (Greedy)")
    print("Chosen items (value, weight):", items)
    print("Maximum value:", max_value)
