def bubble_sort(list):
    n = list.copy()
    for i in range(len(n)):
        for j in range(len(n) - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n


print(bubble_sort([5, 2, 8, 1]))