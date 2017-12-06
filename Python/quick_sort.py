
# ========
# In Place
# ========

def qsort_in_place(array):
    qsort_helper(array,0,len(array)-1)
    return array


def qsort_helper(array,first,last):
    if first < last:

        splitpoint = partition(array,first,last)

        qsort_helper(array,first,splitpoint-1)
        qsort_helper(array,splitpoint+1,last)


def partition(array,first,last):
    pivot_value = array[first]

    left_pointer = first + 1
    right_pointer = last

    done = False
    while not done:

        while left_pointer <= right_pointer and array[left_pointer] <= pivot_value:
            left_pointer += 1

        while array[right_pointer] >= pivot_value and right_pointer >= left_pointer:
            right_pointer -= 1

        if right_pointer < left_pointer:
            done = True
        else:
            temp = array[left_pointer]
            array[left_pointer] = array[right_pointer]
            array[right_pointer] = temp

    temp = array[first]
    array[first] = array[right_pointer]
    array[right_pointer] = temp

    return right_pointer



# ============================================
# More efficient due to randomization of pivot
# ============================================

from random import randint

def qsort_random_pivot(array):
    if len(array) <= 1: return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array)-1)]

    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return qsort_random_pivot(smaller) + equal + qsort_random_pivot(larger)