# merge sort
# time complexity: O(nlogn)
# space complexity: O(n)

def merge_sort(list):
	def merge(lst1, lst2):
		merged_lst = []
		lst1_current = 0
		lst2_current = 0
		
		while len(merged_lst) != len(lst1) + len(lst2):
			if lst2_current == len(lst2):
				merged_lst += lst1[lst1_current:]
			elif lst1_current == len(lst1):
				merged_lst += lst2[lst2_current:]
			elif lst1[lst1_current] > lst2[lst2_current]:
				merged_lst.append(lst2[lst2_current])
				lst2_current += 1
			elif lst1[lst1_current] <= lst2[lst2_current]:
				merged_lst.append(lst1[lst1_current])
				lst1_current += 1 
		
		return merged_lst
	
	if len(list) == 1:
		return list
	else:
		mid = len(list) // 2
		return merge(merge_sort(list[0 : mid]), merge_sort(list[mid : len(list)]))
		
lst = [8, 3, 1, 7, 0, 10, 2]
lst = merge_sort(lst)

print(lst)
