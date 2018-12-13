# python3
import sys

def max_pairwise_product(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers[0] * numbers[1]

if __name__ == '__main__':
    input = sys.stdin.read().splitlines() 
    input_n = int(input[0])
    input_numbers = [int(x) for x in input[1].split(' ')]
    print(max_pairwise_product(input_numbers))
