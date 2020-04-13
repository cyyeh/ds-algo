# Uses python3
import sys

def optimal_sequence(n):
    sequence = [0] * (n + 1)
    sequence[1] = 1
    sequence_dict = {
        "1": [1]
    }

    for i in range(2, n + 1):
        sequence[i] = n + 1
        sequence_dict[str(i)] = []
        if i - 1 > 0:
            num_sequence = sequence[i - 1] + 1
            if num_sequence < sequence[i]:
                sequence[i] = num_sequence
                sequence_dict[str(i)] = sequence_dict[str(i - 1)] + [i]
        if i % 3 == 0:
            num_sequence = sequence[i // 3] + 1
            if num_sequence < sequence[i]:
                sequence[i] = num_sequence
                sequence_dict[str(i)] = sequence_dict[str(i // 3)] + [i]
        if i % 2 == 0:
            num_sequence = sequence[i // 2] + 1
            if num_sequence < sequence[i]:
                sequence[i] = num_sequence
                sequence_dict[str(i)] = sequence_dict[str(i // 2)] + [i]

    return sequence_dict[str(n)]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
