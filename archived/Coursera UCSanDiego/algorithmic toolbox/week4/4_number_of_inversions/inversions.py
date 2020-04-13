# Uses python3
import sys

def get_number_of_inversions(a, left, right):
    def get_number_of_inversions_auxiliary(a, left, right):
        def merge(first, second, number_invertions):
            sorted = []
            
            while len(first) and len(second):
                first_head = first[0]
                second_head = second[0]
                if first_head <= second_head:
                    sorted.append(first_head)
                    first = first[1:]
                else:
                    sorted.append(second_head)
                    second = second[1:]
                    number_invertions += 1 * len(first)
            if len(first):
                sorted += first
            else:
                sorted += second

            return (sorted, number_invertions)

        number_invertions = 0
        if right - left <= 1:
            return (a[left:right], number_invertions)

        ave = (left + right) // 2
        (sorted_first_half, number_of_inversions_first_half) = get_number_of_inversions_auxiliary(a, left, ave)
        (sorted_second_half, number_of_inversions_second_half) = get_number_of_inversions_auxiliary(a, ave, right)

        number_invertions = number_of_inversions_first_half + number_of_inversions_second_half

        return merge(sorted_first_half, sorted_second_half, number_invertions)

    return get_number_of_inversions_auxiliary(a, left, right)[1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    print(get_number_of_inversions(a, 0, len(a)))
