def recur_binary_search(arr, val):
	if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
		return False

	mid = arr[len(arr) // 2]

	if val == mid:
		return True
	elif val < mid:
		return recur_binary_search(arr[:len(arr) // 2], val)
	elif val > mid:
		return recur_binary_search(arr[len(arr) // 2 + 1:], val)
	else:
		return False


def iter_binary_search(arr, val):
	if not arr or (len(arr) == 1 and arr[0] is not val):
		return False

	low, high = 0, len(arr) - 1

	while low <= high:
		mid = (low + high) // 2
		if val == arr[mid]:
			return True
		elif val < arr[mid]:
			high = mid - 1
		elif val > arr[mid]:
			low = mid + 1
	return False

arr = [-1, 0, 3, 5, 7, 8, 9, 10, 14, 24, 47, 79]
arr2 = []
arr3 = [5]

print(recur_binary_search(arr, -1))  # True
print(recur_binary_search(arr, 4))   # False

print(recur_binary_search(arr2, 5))  # False
print(recur_binary_search(arr3, 5))  # True

print(iter_binary_search(arr, -1))   # True
print(iter_binary_search(arr, 4))    # False

print(iter_binary_search(arr2, 5))   # False
print(iter_binary_search(arr3, 5))   # True
