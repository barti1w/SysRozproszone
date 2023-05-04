def zad1():
    def extract_numbers(values: list[any]) -> list[int | float]:
        return list(filter(isIntFloat, values))

    def isIntFloat(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False

    values = [1, 2, "Ala", 1.2, "O"]

    print(extract_numbers(values))

def zad2():
    a = input()
    b = input()
    c = input()

    lista = [a, b, c]

    print(sorted(lista, key=lambda x: len(x)))

def zad3():
    lista = ["Ala", 1, 3, 2, "ma", "kota"]
    sorted_list = sorted(lista, key=lambda x: (isinstance(x, str), x), reverse=True)
    print(sorted_list)

import csv
import datetime
import unicodedata

def zad4():
    def clean_data(row):
        utarg = str(row['Utarg'])
        utarg = utarg.replace("z", "").replace(",", ".").replace(" ", "")
        row['Utarg'] = utarg

        dat = str(row['Data zamowienia']).split(".")
        newDate = datetime.date(int(dat[2]), int(dat[1]), int(dat[0]))
        row['Data zamowienia'] = str(newDate)

        return row

    def save_to_file(row):
        if row['Kraj'] == 'Polska':
            with open('zamowienia_polska.csv', 'a+', encoding='utf-8', errors='ignore', newline='') as csvfilePoland:
                writer = csv.DictWriter(csvfilePoland,
                                        fieldnames=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
                if csvfilePoland.tell() == 0:
                    writer.writeheader()
                writer.writerow(row)
        elif row['Kraj'] == 'Niemcy':
            with open('zamowienia_niemcy.csv', 'a+', encoding='utf-8', errors='ignore', newline='') as csvfileGermany:
                writer = csv.DictWriter(csvfileGermany,
                                        fieldnames=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
                if csvfileGermany.tell() == 0:
                    writer.writeheader()
                writer.writerow(row)

    with open('zamowienia.csv', encoding='utf-8-sig', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = list(reader)

        cleaned_rows = map(clean_data, rows)
        for row in cleaned_rows:
            save_to_file(row)

def zad5():
    def sort_dict_by_func(dictionary, func):
        return dict(sorted(dictionary.items(), key=lambda item: func(item[1])))

    dictionary = {'Jan': [0, 3, 4, 10], 'Anna': [2, 5, 6, 9], 'Kasia': [2, 4, 6, 8]}
    print(sort_dict_by_func(dictionary, min))
    print(sort_dict_by_func(dictionary, max))
    print(sort_dict_by_func(dictionary, sum))

zad1()
zad2()
zad3()
zad4()
zad5()