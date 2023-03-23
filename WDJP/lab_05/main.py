# Zad 1

import math
import random

A = [1 / i for i in range(1, 10)]
B = [math.pow(2, i) for i in range(0, 10)]
C = [x for x in B if x % 4 == 0]
print(A, B, C)

# Zad 2

matrix = [[random.randint(0, 10) for x in range(4)] for y in range(4)]
print(matrix)

diagonal = [num for row in matrix for num in row if row.index(num) == matrix.index(row)]
print(diagonal)

# Zad 3

strin = "Ala ma kota"

output = [(x, [ord(y) for y in x]) for x in strin.split(" ")]
print(output)

# Zad 4

import math
from typing import Union

Num = Union[int, float]


def row_kwadratowe(a: Num, b: Num, c: Num):
    delta = b ** 2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2


print(row_kwadratowe(6, 1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))


# Zad 5

def dice(n: int):
    result = []
    for i in range(n):
        eye = random.randint(1, 6)
        result.append(("oczka: " + str(eye), "rzutów: " + str(i + 1)))

    print(result)


dice(5)


# Zad 6
def ciag(*words: str):
    listWords = list(words)
    return sorted(listWords)


# podajemy argumenty
print(ciag('aaa', 'ccc', 'bbb', 'dddd', 'ggg', 'eee'))


# Zad 7

def sum_points(**clubs):
    result = 0
    for club in clubs:
        result += clubs[club]
    print(f'Suma wszystkich punktów {result}.')


sum_points(stomilOlsztyn=10, legiaWarszawa=20, wislaKrakow=25)
