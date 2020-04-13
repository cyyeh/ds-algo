# Uses python3

def get_change(m):
    denominations = {
        "1": 1,
        "5": 5,
        "10": 10
    }
    minimum_coins = 0

    while m > 0:
        if m >= denominations["10"]:
            m -= 10
        elif m >= denominations["5"]:
            m -= 5
        else:
            m -= 1
        minimum_coins += 1
    
    return minimum_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m)) 