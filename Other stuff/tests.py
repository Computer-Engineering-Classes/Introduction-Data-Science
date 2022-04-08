import math
import time
import numpy as np


class Temperatura:

    def __init__(self, temperatura: float) -> None:
        self.temperatura = temperatura

    @property
    def temperatura(self) -> float:
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 ºC is not possible")
        self._temperatura = value

    def show(self) -> None:
        print(f"Temp = {self.temperatura} ºC")


if __name__ == "__main__":
    l = []
    for i in range(3000):
        l.append([])
        for j in range(3000):
            l[i].append(j)

    start = time.perf_counter()
    for i, row in enumerate(l):
        for j, el in enumerate(row):
            row[j] = math.sqrt(el)
    end = time.perf_counter()
    print(f"Using lists and enumerate: {end - start}")

    l = np.array(l)

    start = time.perf_counter()
    l = np.sqrt(l)
    end = time.perf_counter()
    print(l.shape)
    print(f"Using NumPy: {end - start}")

    s = {1, 4, 2, 4, -5, 2}

    d = {70633: "Diogo", 70648: "Rui", 70579: "João"}
