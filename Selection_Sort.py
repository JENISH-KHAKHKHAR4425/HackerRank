def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
sample_array = [5, 2, 9, 1, 5, 6]

print("Original Array:", sample_array)
print("\nSelection Sort Result:")
print(selection_sort(sample_array.copy()))