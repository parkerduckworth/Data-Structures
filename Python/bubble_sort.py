def bubble_sort(L):
    for i in range(0, len(L) - 1):
        for j in range(0, len(L) - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L