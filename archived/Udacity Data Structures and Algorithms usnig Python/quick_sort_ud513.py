# quick sort
# worst-case time complexity: O(n^2)
# average-case time complexity: O(nlogn)
# best-case time complexity: O(nlogn)
# in-place sorting algorithm: O(1)
def do_quicksort(lst, lo, hi):
	if lo < hi:
		p = partition(lst, lo, hi)
		do_quicksort(lst, lo, p)
		do_quicksort(lst, p+1, hi)
	return

def partition(lst, lo, hi):
	pivot = lst[hi-1] # choose last element of array as pivot
	i = lo - 1
	for j in range(lo, hi):
		if lst[j] < pivot:
			i += 1
			lst[i], lst[j] = lst[j], lst[i]
	if lst[hi-1] < lst[i+1]:
		lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
	return i+1

def quicksort(array):
	do_quicksort(array, 0, len(array))
	
	return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))

# pivot: 14
# [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# [21, 4, 1, 3, 9, 20, 25, 6, 14, 21]
# [6, 4, 1, 3, 9, 20, 25, 14, 21, 21]
# [25, 6, 4, 1, 3, 9, 14, 20, 21, 21]
# [9, 6, 4, 1, 3, 14, 25, 20, 21, 21]
