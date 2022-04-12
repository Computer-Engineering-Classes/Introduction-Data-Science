import time
import numpy as np
from numpy import ndarray


def sum_of_multiples(x: int, y: int, limit: int) -> ndarray:
    ln = np.arange(1, limit)
    multiples = ln[np.where((ln % x == 0) | (ln % y == 0))]
    return np.sum(multiples, dtype=np.int64)


def sum_of_multiplesv2(x, y, limit):
    return sum([i for i in range(1, limit) if (i % x == 0) or (i % y == 0)])


if __name__ == '__main__':
    start = time.perf_counter()
    print(sum_of_multiples(3, 5, 1000))
    end = time.perf_counter()
    print(end - start)
    start = time.perf_counter()
    print(sum_of_multiplesv2(3, 5, 1000))
    end = time.perf_counter()
    print(end - start)
