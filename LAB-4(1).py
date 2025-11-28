# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Conquer (merge the sorted halves)
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0
    
    # Compare and merge elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


# Example run
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original Array:", arr)
    print("Sorted Array (Merge Sort):", merge_sort(arr))
