# Uses python3

def get_fibonacci_mod_m(n, m):
    if n <= 1:
        return n

    fib_list = [0, 1]
    fib_mod_m_list = [0, 1]
    i = 2

    while True:
        if len(fib_mod_m_list) > 2 and fib_mod_m_list[-2:] == [0, 1]:
            fib_mod_m_list = fib_mod_m_list[0 : -2]
            break
        elif (i - 1) == n:
            return fib_mod_m_list[-1]

        next = fib_list[i - 1] + fib_list[i - 2]
        fib_mod_m_list.append(next % m)
        fib_list.append(next)
        i += 1

    remainder = n % len(fib_mod_m_list)
    return fib_mod_m_list[remainder]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_mod_m(n, m))
