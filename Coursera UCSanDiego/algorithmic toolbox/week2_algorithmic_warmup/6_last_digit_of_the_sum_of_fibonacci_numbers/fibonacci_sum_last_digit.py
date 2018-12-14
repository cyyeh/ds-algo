# Uses python3

def fibonacci_sum_last_digit(n):
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
    if n <= 1:
        return n

    f_n_plus_2 = get_fibonacci_mod_m(n + 2, 10)
    if f_n_plus_2 == 0:
        return 9
    else:
        return f_n_plus_2 - 1

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_last_digit(n))
