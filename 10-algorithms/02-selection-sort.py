def selection_sort(ls):
    for i in range(0, len(ls)):
        min_idx = i
        for j in range(i + 1, len(ls)):
            if ls[min_idx] > ls[j]:
                min_idx = j
        ls[i], ls[min_idx] = ls[min_idx], ls[i]

    return ls


print(selection_sort([4, 3, 6, 10, 1]))
# i = 0, j = 1, min_idx = 1
# i = 0, j = 4, min_idx = 4
# 1, 3, 6, 10, 4; i = 0
# i = 1, j = 2, min_idx = 1
# i = 2, j = 3, min_idx = 2
# i = 2, j = 4, min_idx = 4
# 1, 3, 4, 10, 6; i = 2
