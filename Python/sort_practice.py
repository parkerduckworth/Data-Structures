import random


def generate_int_list(list_length):
    res = []
    for i in range(list_length):
        res.append(random.randrange(-10, 10))
    return res


def bucket_sort(L):
    elems, counter = [0] * (max(L) + 1), [0] * (max(L) + 1)
    for i in range(len(L)):
        elems[L[i]], counter[L[i]] = L[i], counter[L[i]] + 1
    res = [[e] * i for e, i in zip(elems, counter) if i != 0]
    return [inner for outer in res for inner in outer]


def bubble_sort(L):
    n = len(L) - 1
    for i in range(n):
        for j in range(n - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


def selection_sort(L):
    n = len(L)
    for i in range(n - 1):
        minimum = i
        for j in range(i + 1, n):
            if L[j] < L[minimum]:
                minimum = j
        L[i], L[minimum] = L[minimum], L[i]
    return L


def insertion_sort(L):
    for i in range(len(L) - 1):
        p = i + 1
        while p >= 1:
            if L[p] < L[p - 1]:
                L[p], L[p - 1] = L[p - 1], L[p]
            p -= 1
    return L


def merge_sort(L):
    if len(L) > 1:
        mid = len(L) // 2
        left_half, right_half = L[:mid], L[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                L[k], i = left_half[i], i + 1
            else:
                L[k], j = right_half[j], j + 1
            k += 1
        while i < len(left_half):
            L[k] = left_half[i]
            i, k = i + 1, k + 1
        while j < len(right_half):
            L[k] = right_half[j]
            j, k = j + 1, k + 1
    return 


merge_sort(generate_int_list(15000))
