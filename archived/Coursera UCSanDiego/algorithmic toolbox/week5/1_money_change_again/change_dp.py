# Uses python3
import sys

def get_change(money):
    min_num_coins = [0 for _ in range(money + 1)]
    coins = [1, 3, 4]

    for m in range(1, money + 1):
        min_num_coins[m] = 1001
        for i in range(len(coins)):
            if m >= coins[i]:
                num_coins = min_num_coins[m - coins[i]] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
