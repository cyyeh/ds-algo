# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    # [(value, weight, value_per_weight),...]
    value_weight_tuple_list = [value_weight_pair + (value_weight_pair[0] / value_weight_pair[1],) for value_weight_pair in zip(values, weights)]
    # sort in descending order based on value per weight unit
    value_weight_tuple_list = sorted(value_weight_tuple_list, key = lambda x: x[-1], reverse = True)
    # greedy algorithm for the fractional knapsack problem
    current_weight = 0
    current_value = 0
    for item in value_weight_tuple_list:
        if current_weight + item[1] <= capacity:
            current_weight += item[1]
            current_value += item[0]
        else:
            current_value += (capacity - current_weight) * item[2]
            current_weight = capacity

        if current_weight == capacity:
            break

    return current_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
