def quick_sort(lst, choosing_pivot = "first"):
    def inplace_quick_sort(lst, left, right):
        def partition(lst, l, r):
            pivot = lst[l]
            i = l + 1
            
            for j in range(l+1, r):
                if lst[j] < pivot:
                    lst[j], lst[i] = lst[i], lst[j]
                    i += 1
            lst[l], lst[i-1] = lst[i-1], lst[l]
            
            return i - 2, i

        if left >= right:
            return lst
        else:
            # choose  pivot
            if choosing_pivot == "first":
                pass
            elif choosing_pivot == "last":
                lst[left], lst[right-1] = lst[right-1], lst[left]
            elif choosing_pivot == "middle":
                first = lst[left]
                last = lst[right-1]

                if (right - left) % 2 == 1:
                    middle = lst[left + (right - 1 - left)//2]

                    if (first >= middle and middle >= last) or (last >= middle and middle >= first):
                        lst[left], lst[left + (right - 1 - left)//2] = lst[left + (right - 1 - left)//2], lst[left]
                    elif (first >= last and last >= middle) or (middle >= last and last >= first):
                        lst[left], lst[right-1] = lst[right-1], lst[left]
                else:
                    middle = lst[left + (right - left)//2 - 1]

                    if (first >= middle and middle >= last) or (last >= middle and middle >= first):
                        lst[left], lst[left + (right - left)//2 - 1] = lst[left + (right - left)//2 - 1], lst[left]
                    elif (first >= last and last >= middle) or (middle >= last and last >= first):
                        lst[left], lst[right-1] = lst[right-1], lst[left]
            
            # partition lst around pivot, assume pivot is at the first position of lst
            nonlocal num_comparisons
            num_comparisons += (right - left - 1)
            left_high, right_low = partition(lst, left, right)
            inplace_quick_sort(lst, left, left_high+1)
            inplace_quick_sort(lst, right_low, right)
            return lst
    
    num_comparisons = 0
    inplace_quick_sort(lst, 0, len(lst))
    return num_comparisons


f = open('quick_sort.txt')
lines = f.readlines()
lst = []
for line in lines:
    lst.append(int(line))
f.close()

num_comparisons = quick_sort(lst, "middle")
print(num_comparisons)

# first=> comparisons: 162085
# last=> comparisons: 164123
# middle=> comparisons: 138382