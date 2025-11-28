def counting_sort(arr):
    if not arr:
        return []
    if min(arr) < 0:
        raise ValueError("Counting sort only works with non-negative integers")
    
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    index = 0
    for i, c in enumerate(count):
        for _ in range(c):
            arr[index] = i
            index += 1
    return arr

sample_array = [5, 2, 9, 1, 5, 6]

print("Original Array:", sample_array)
print("\nCounting Sort Result:")
print(counting_sort(sample_array.copy()))