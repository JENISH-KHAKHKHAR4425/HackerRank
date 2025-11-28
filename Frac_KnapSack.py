def fractional_knapsack(capacity, weights, values):
    # Calculate the value-to-weight ratio for each item
    ratios = [value / weight for value, weight in zip(values, weights)]
    # Sort the items based on the value-to-weight ratio in descending order
    sorted_items = sorted(zip(ratios, weights, values), reverse=True)
    total_value = 0.0
    for ratio, weight, value in sorted_items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            total_value += value * fraction
            break
    return total_value