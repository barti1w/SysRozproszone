import csv
import datetime
import unicodedata
#Zad 1

# with open('zamowienia.csv', encoding='utf-8-sig', errors='ignore') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=';')
#     for row in reader:
#         utarg = str(row['Utarg'])
#         utarg = utarg.replace("z", "").replace(",", ".").replace(" ", "")
#         row['Utarg'] = utarg
#
#         dat = str(row['Data zamowienia']).split(".")
#         newDate = datetime.date(int(dat[2]), int(dat[1]), int(dat[0]))
#         row['Data zamowienia'] = str(newDate)
#         if row['Kraj'] == 'Polska':
#             with open('zamowienia_polska.csv', 'a+', encoding='utf-8', errors='ignore', newline='') as csvfilePoland:
#                 writer = csv.DictWriter(csvfilePoland, fieldnames=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
#                 if csvfilePoland.tell() == 0:
#                     writer.writeheader()
#                 writer.writerow(row)
#         elif row['Kraj'] == 'Niemcy':
#             with open('zamowienia_niemcy.csv', 'a+', encoding='utf-8', errors='ignore', newline='') as csvfileGermany:
#                 writer = csv.DictWriter(csvfileGermany, fieldnames=['Kraj', 'Sprzedawca', 'Data zamowienia', 'idZamowienia', 'Utarg'])
#                 if csvfileGermany.tell() == 0:
#                     writer.writeheader()
#                 writer.writerow(row)

#Zad 2
def zad2(listOfFiles, nameOfNewFile):
    with open(nameOfNewFile, 'a+') as newFile:
        for file in listOfFiles:
            with open(file, 'r') as oldFile:
                newFile.write(oldFile.read())

# zad2(['text1.txt', 'text2.txt', 'text3.txt'], 'result.txt')

#Zad 3
def zad3(inputList, n, shouldReturnMinNumbers):
    listOfNumbers = []
    for x in inputList:
        if type(x) == int:
            listOfNumbers.append(x)

    if shouldReturnMinNumbers:
        listOfNumbers.sort()
    else:
        listOfNumbers.sort(reverse=True)

    resultList = listOfNumbers[:n]
    print(resultList)

# zad3(['a', 12, 23, 1, 2, 0, -5], 2, False)

#Zad 4
def zad4(inputList):
    dictWithTypes = {}
    for x in inputList:
        if type(x) not in dictWithTypes.keys():
            dictWithTypes[type(x)] = x
        else:
            dictWithTypes.update({type(x): [dictWithTypes[type(x)], x]})
    print(dictWithTypes)

# zad4([1, 2.3, 'Zbyszek', 5, 'Marian', 3.0])

#Zad 5
def zad5(listOfSurnames):
    listToM = []
    listFromM = []
    for x in listOfSurnames:
        if ord(x[0]) < 78:
            listToM.append(x)
        else:
            listFromM.append(x)

    with open('A-M_nazwiska.txt', 'a+') as amFile:
        for i in listToM:
            amFile.write(i + '\n')

    with open('N-Ż_nazwiska.txt', 'a+') as nzFile:
        for i in listFromM:
            nzFile.write(i + '\n')

zad5(['Abb', 'Mmm', 'Zzz', 'Ooo', 'Bbb'])