def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
unsorted_data = [4, 2, 7, 1, 9, 5]
sorted_data = sorted(unsorted_data)
target = 5

print("Original (Unsorted) Array:", unsorted_data)
index_linear = linear_search(unsorted_data, target)
print(f"Linear Search: Element {target} found at index {index_linear}" if index_linear != -1 else "Element not found")