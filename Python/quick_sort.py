
from random import randint

def quick_sort(L):
    if len(L) <= 1: 
        return L
    smaller, equal, larger = [], [], []
    pivot = L[randint(0, len(L)-1)]

    for x in L:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)


L = [-1000, 0, 9999, 43, -22, 53, 76, 3, 98, 113, -435, 0, 5]

print(quick_sort(L)) # [-1000, -435, -22, 0, 0, 3, 5, 43, 53, 76, 98, 113, 9999]