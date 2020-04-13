# Uses python3

def fibonacci_partial_sum(from_, to):
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
    
    # f_n+2 - 1
    f_n = get_fibonacci_mod_m(to + 2, 10)
    if f_n == 0:
        f_n = 9
    else:
        f_n = f_n - 1

    f_m_minus_one = get_fibonacci_mod_m(from_ + 1, 10)
    if f_m_minus_one == 0:
        f_m_minus_one == 9
    else:
        f_m_minus_one = f_m_minus_one - 1
    
    if f_n < f_m_minus_one:
        return 10 - f_m_minus_one + f_n
    else:
        return f_n - f_m_minus_one


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))