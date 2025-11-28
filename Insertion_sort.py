def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
sample_array = [5, 2, 9, 1, 5, 6]

print("Original Array:", sample_array)

print("\nInsertion Sort Result:")
print(insertion_sort(sample_array.copy()))