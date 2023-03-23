# Zad 1
import random

number = input()
number = int(number)
print(bin(number))
print(oct(number))
print(hex(number))

# Zad 2

i = input()

try:
    int(i)
    print("Can be cast to int")
except:
    print("Cannot cast to int")

try:
    float(i)
    print("Can be cast to int")
except:
    print("Cannot cast to float")

# Zad 3

import sys
import math

num = sys.stdin.readline()
result = ""
times = 0
num = int(num)

while num > 0:
    remain = num % 10
    num = num-remain
    num = num / 10
    plusSign = " + "
    if num == 0:
        plusSign = ""
    result = result + str(math.pow(10, times)) + " * " + str(remain) + plusSign
    times += 1

sys.stdout.write("Podaną liczbę można zapisać jako: " + result)

# Zad 4

s = input()

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in s]))

# Zad 5

sentence = input()
words = sentence.split(" ")
bigToSmallWords = sorted(words, key=len)
print(bigToSmallWords)

# Zad 6

col_1 = ['Koleżanki i koledzy', 'Z drugiej strony', 'Podobnie', 'Nie zapominajmy jednak, że', 'W ten oto sposób',
         'Praktyka dnia codziennego dowodzi, że',
         'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
         'Różnorakie i bogate doświadczenia', 'Troska organizacji, a szczególnie', 'Wyższe założenia ideowe, a także',
         'rozpoczęcie powszechnej akcji kształtowania postaw']
col_2 = ['realizacja nakreślonych zadań programowych', 'zakres i miejsce szkolenia kadr',
         'stały wzrost ilości i zakres naszej aktywności', 'aktualna struktura organizacji',
         'nowy model działalności organizacyjnej', 'dalszy rozwój różnych form działalności',
         'stałe zabezpieczenie informacyjno programowe naszej działalności', 'wzmacnianie i rozwijanie struktur',
         'konsultacja z szerokim aktywem', 'rozpoczęcie powszechnej akcji kształtowania postaw',
         'proces wdrażania i unowocześniania']
col_3 = ['zmusza nas do przeanalizowania', 'spełnia istotną rolę w kształtowaniu', 'wymaga sprecyzowania i określenia',
         'pomaga w przygotowaniu i realizacji', 'zabezpiecza udział szerokiej grupie w kształtowaniu',
         'spełnia ważne zadania w wypracowaniu', 'umożliwia w większym stopniu tworzenie',
         'powoduje docenianie wagi', 'przedstawia intersującą próbę sprawdzenia',
         'pociąga za sobą proces wdrażania i unowocześniania']
col_4 = ['istniejących warunków administracyjno-finansowych.', 'dalszych kierunków rozwoju.',
         'systemu powszechnego uczestnictwa.', 'postaw uczestników wobec zadań stawianych przez organizację.',
         'nowych propozycji.', 'kierunków postępowego wychowania.',
         'systemu szkolenia kadry odpowiadającego potrzebom.', 'odpowiednich waruknków aktywizacji.',
         'modelu rozwoju.', 'form oddziaływania.']

n = input()
n = int(n)

for i in range(n):
    print(str(random.choice(col_1)) + " " + str(random.choice(col_2)) + " " + str(random.choice(col_3)) + " " + str(random.choice(col_4)))

