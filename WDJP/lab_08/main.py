from timeit import timeit
from array import array
import random
from datetime import datetime

# Zad1
setup = """
from array import array
import random
"""

stmt1 = """
array_of_ints = array('i', [random.randint(1, 1000) for _ in range(10_000)])
"""

stmt2 = """
list_of_ints = [random.randint(1, 10000) for _ in range(10_000)]
"""

stmt3 = """
array_of_longs = array('q', [random.randint(1, 10000) for _ in range(10_000)])
"""

stmt4 = """
list_of_longs = [random.randint(1, 10000) for _ in range(10_000)]
"""

stmt5 = """
array_of_chars = array('u', ['a' for _ in range(10_000)])
"""

stmt6 = """
list_of_chars = ['a' for _ in range(10_000)]
"""

print("Array int: ", timeit(stmt1, setup, number=100))
print("List int: ", timeit(stmt2, setup, number=100))
print("Array long: ", timeit(stmt3, setup, number=100))
print("List long: ", timeit(stmt4, setup, number=100))
print("Array chars: ", timeit(stmt5, setup, number=100))
print("List chars: ", timeit(stmt6, setup, number=100))

# Zad2


startArray = datetime.now()

tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)

tab_of_floats_loaded = array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()

endArray =  datetime.now() - startArray
startList = datetime.now()

list_of_floats = [random.random() for _ in range(1_000_000)]
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))

with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
print(list_of_floats_loaded[:10])

endList = datetime.now() - startList
print("Time for list: ", endList)
print("Time for array: ", endArray)


from collections import deque, namedtuple, Counter


def test_deque():
    kolejka = deque('Ala ma kota'.split())
    print(kolejka)

    kolejka.append('Czy')
    print(kolejka)

    kolejka.appendleft('Czy')
    print(kolejka)

def test_deque():
    kolejka = deque('Ala ma kota'.split())
    start = datetime.now()
    kolejka.append('Czy')
    end1 = datetime.now() - start
    kolejka.appendleft('Czy')
    end2 = datetime.now() - start + end1
    print("append: ", end1)
    print("appendLeft: ", end2)

def test_lists():
    lista = [x for x in range(100_000_000)]
    start = datetime.now()
    lista.append(1)
    end1 = datetime.now() - start
    lista.insert(0, 1)
    end2 = datetime.now() - start + end1
    print("append: ", end1)
    print("insert: ", end2)

test_deque()
test_lists()

def zad5(tablica: list):
    tablica.sort()
    howMany = int(len(tablica)/10)
    print(tablica[howMany:howMany+1:])

zad5([1,2,3,4,5,6,7,8,9,10,0,2,1])


import csv

with open('zamowienia.csv', encoding='utf-8-sig', errors='ignore') as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader)
    data = []
    for row in reader:
        named_tuple = tuple(zip(header, row))
        data.append(dict(named_tuple))

for d in data[:5]:
    print(d)