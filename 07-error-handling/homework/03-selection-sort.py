def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([5, 3, 10, 10, 1]))
print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([10, -1, -5, -10, 0]))
print(selection_sort([5]))
print(selection_sort([]))
print(selection_sort([5, 4, 3, 2, 1]))

# min_index = 0
# [1, 3, 10, 10, 5]
# [1, 3, 10, 10, 5]
# [1, 3, 5, 10, 10]
# [1, 3, 5, 10, 10]
