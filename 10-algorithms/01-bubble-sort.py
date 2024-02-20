def bubble_sort(ls):
    for i in range(0, len(ls)):
        for j in range(0, len(ls)):
            if ls[i] < ls[j]:
                ls[i], ls[j] = ls[j], ls[i]

    return ls


print(bubble_sort([4, 3, 6, 10, 1]))
# 4, 3, 6, 10, 1; i = 0, j = 0
# 6, 3, 4, 10, 1; i = 0, j = 2
# 10, 3, 4, 6, 1; i = 0, j = 3
# 3, 10, 4, 6, 1; i = 1, j = 0
# 3, 4, 10, 6, 1; i = 2, j = 1
# 3, 4, 6, 10, 1; i = 3, j = 2
# 1, 4, 6, 10, 3; i = 4, j = 0
# 1, 3, 6, 10, 4; i = 4, j = 1
# 1, 3, 4, 10, 6; i = 4, j = 2
# 1, 3, 4, 6, 10; i = 4, j = 3
