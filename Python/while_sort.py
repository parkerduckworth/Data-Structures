def sort(L):
    n = len(L) - 1
    while n:
        for i in range(n):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        n -= 1
    return L


L = [3, 5, -1, 0, 44, 99, -300, -10000, 12222, 43.3]

print(sort(L)) # [-10000, -300, -1, 0, 3, 5, 43.3, 44, 99, 12222]