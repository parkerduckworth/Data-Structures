def insertion_sort(list_):
    for i in range(len(list_)):
        j = i
        while j > 0 and (list_[j] < list_[j - 1]):
            list_[j], list_[j - 1] = list_[j - 1], list_[j]
            j = j - 1
    return list_