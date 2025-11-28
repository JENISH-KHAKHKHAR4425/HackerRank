# Linear Search
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

# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
unsorted_data = [4, 2, 7, 1, 9, 5]
sorted_data = sorted(unsorted_data)
target = 5
print("\nSorted Array:", sorted_data)
index_binary = binary_search(sorted_data, target)
print(f"Binary Search: Element {target} found at index {index_binary}" if index_binary != -1 else "Element not found")
