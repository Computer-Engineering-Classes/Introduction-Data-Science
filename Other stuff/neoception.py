import math
import numpy as np


def fact(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def sum_sq_diff(n: int) -> int:
    ln = np.arange(n + 1)
    sum_of_sq = np.sum(ln ** 2)
    sq_of_sum = np.sum(ln) ** 2
    return sq_of_sum - sum_of_sq


if __name__ == '__main__':
    x = 52
    print(f'Factorial of {x=} ({fact.__name__}): {fact(x)}')
    print(f'Factorial of {x=} ({math.factorial.__name__}): {math.factorial(x)}')
    n = 10
    print(f'Sum square difference {n=}: {sum_sq_diff(n)=}')
    n = 100
    print(f'Sum square difference {n=}: {sum_sq_diff(n)=}')
