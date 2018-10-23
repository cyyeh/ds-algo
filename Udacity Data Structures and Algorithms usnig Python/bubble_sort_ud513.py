# bubble sort
# worst-case time complexity: O(n^2)
# average-case time complexity: O(n^2)
# best-case time complexity: O(n)
# in-place sorting -> space complexity: O(n)

def bubble_sort(list):
	for j in range(len(list) - 1):
		for i in range(len(list) - 1):
			if i + 1 < len(list) and list[i + 1] < list[i]:
				list[i + 1], list[i] = list[i], list[i + 1]
		print(list)
	
lst = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
bubble_sort(lst)
