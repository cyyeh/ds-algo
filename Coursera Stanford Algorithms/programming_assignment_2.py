def count_inversions(lst):
    def sort_and_count(lst):
        if len(lst) == 1:
            return lst, 0
        else:
            mid = len(lst) // 2
            sorted_lst_firsthalf, inversion_counts_firsthalf = sort_and_count(lst[:mid])
            sorted_lst_secondhalf, inversions_counts_secondhalf = sort_and_count(lst[mid:])
            sorted_lst, inversion_counts_mid = count_split_inversions(sorted_lst_firsthalf, sorted_lst_secondhalf)
        return sorted_lst, inversion_counts_firsthalf + inversions_counts_secondhalf + inversion_counts_mid

    def count_split_inversions(lst1, lst2):
        merged_list = []
        lst1_current = 0
        lst2_current = 0
        inversion_counts = 0

        while len(merged_list) != len(lst1) + len(lst2):
            if lst2_current == len(lst2):
                merged_list += lst1[lst1_current:]
            elif lst1_current == len(lst1):
                merged_list += lst2[lst2_current:]
            elif lst1[lst1_current] > lst2[lst2_current]:
                merged_list.append(lst2[lst2_current])
                lst2_current += 1
                inversion_counts += (len(lst1) - lst1_current)
            elif lst1[lst1_current] <= lst2[lst2_current]: 
                merged_list.append(lst1[lst1_current])
                lst1_current += 1

        return merged_list, inversion_counts

    return sort_and_count(lst)

f = open('integer_array.txt')
lines = f.readlines()
lst = []
for line in lines:
    lst.append(int(line))
f.close()


lst, count_inversions = count_inversions(lst)
print(count_inversions)