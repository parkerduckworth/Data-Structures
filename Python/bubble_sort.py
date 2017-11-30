def bubble_sort(list_):
    for i in range(0, len(list_) - 1):
        for j in range(0, len(list_) - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


a = [5, 3, 7, 5, 8, 1, 5, 9, 2, 0]
print(bubble_sort(a))