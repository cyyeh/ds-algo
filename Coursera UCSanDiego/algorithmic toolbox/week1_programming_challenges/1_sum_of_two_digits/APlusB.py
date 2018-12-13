# python3
import sys

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    input = sys.stdin.readlines()
    a, b = map(int, input[0].split(' '))
    print(sum_of_two_digits(a, b))
