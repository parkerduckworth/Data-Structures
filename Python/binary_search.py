def binary_search(arr, val):
	if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
		return False

	mid = arr[len(arr) // 2]

	if val == mid:
		return True
	if val < mid:
		return binary_search(arr[:len(arr) // 2], val)
	if val > mid:
		return binary_search(arr[len(arr) // 2 + 1:], val)


arr = [1, 4, 6, 44, 243, 6754, 2, 65]
print(binary_search(arr, 1000)) # False
print(binary_search(arr, 1)) # True
print(binary_search(arr, -1)) # False
print(binary_search(arr, 44)) # True
print(binary_search(arr, 0)) # False