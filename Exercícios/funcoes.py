import math as m
import numpy as np


def add_2_values(x1: float, x2: float) -> float:
    return x1 + x2


x = float(input("x = "))
y = float(input("y = "))
print(f"Total = {add_2_values(x, y)}")

print(m.comb(52, 7))
a = np.arange(21)
b = np.sqrt(a)
print(b)

ar = np.array([[4, 5, 6], [3, 8, 7], [2, 0, 9],
              [9, 0, 0], [3, 2, 1], [6, 1, 1]])
print(ar.shape)
for row in ar:
    print(row)
print(f"{ar[3:5]=}")
print(f"{ar[::2]=}")
print(f"{ar[1::3]=}")
print(f"{ar[3::]=}")
