# Activity Selection Problem using Greedy Approach

def activity_selection(start, finish):
    n = len(finish)

    # Step 1: Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    # Step 2: Select first activity
    selected = [activities[0]]
    last_finish = activities[0][1]

    # Step 3: Iterate through remaining activities
    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected

# Driver Code
if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]

    result = activity_selection(start, finish)
    print("Selected Activities (start, finish):", result)
