# Fractional Knapsack using Greedy Approach
def fractional_knapsack(values, weights, capacity):
    n = len(values)
    
    # Calculate value-to-weight ratio
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    # Sort by ratio (descending order)
    ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    chosen_items = []
    
    for r, v, w in ratio:
        if w <= capacity:
            chosen_items.append((v, w, 1))  # take full item
            total_value += v
            capacity -= w
        else:
            fraction = capacity / w
            chosen_items.append((v, w, fraction))  # take fraction of item
            total_value += v * fraction
            break
    
    return total_value, chosen_items


# Example Run
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    
    max_value, items = fractional_knapsack(values, weights, capacity)
    
    print("\nFractional Knapsack (Greedy)")
    print("Chosen items (value, weight, fraction):", items)
    print("Maximum value:", max_value)
