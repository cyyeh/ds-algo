# Uses python3
import sys

def get_majority_element(a, left, right):
    def get_majority_element_auxiliary(a, left, right):
        def merge(first, second):
            merged = first[1] + second[1]

            # both have the same majority or no majority
            if first[0] == second[0]:
                if first[0] != -1:
                    return (first[0], merged)
                else:
                    return (-1, merged)
            else:
                # only the first has the majority
                if first[0] != -1 and (merged).count(first[0]) > (len(merged) // 2):
                    return (first[0], merged)
                # only the second has the majority
                elif second[0] != -1 and (merged).count(second[0]) > (len(merged) // 2):
                    return (second[0], merged)
                else:
                    return (-1, merged)

        if left == right:
            return (-1, [])
        elif left + 1 == right:
            return (a[left], a[left : right])
        
        mid = left + (right - left) // 2
        first_half = get_majority_element_auxiliary(a, left, mid)
        second_half = get_majority_element_auxiliary(a, mid, right)
        return merge(first_half, second_half)

    return get_majority_element_auxiliary(a, left, right)[0]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
