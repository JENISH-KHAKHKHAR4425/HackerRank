# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (middle element for simplicity)
    pivot = arr[len(arr) // 2]
    
    # Partition into three lists
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively apply quick sort
    return quick_sort(left) + middle + quick_sort(right)


# Example run
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original Array:", arr)
    print("Sorted Array (Quick Sort):", quick_sort(arr))
