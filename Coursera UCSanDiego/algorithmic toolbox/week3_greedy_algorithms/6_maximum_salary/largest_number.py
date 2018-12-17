#Uses python3
import sys

def largest_number(digits):
    def is_greater_or_equal(digit, max_digit):
        return True if digit + max_digit > max_digit + digit else False

    result = ''

    while digits:
        max_digit = '0'
        for digit in digits:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        result += max_digit
        digits.remove(max_digit)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    digits = data[1:]
    print(largest_number(digits))
    
