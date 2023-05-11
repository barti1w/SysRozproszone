import os
import csv
def zad1(listOfDir):
    path = ''
    for dir in listOfDir:
        path = os.path.join(path, dir)
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
            print('Created folder: ' + path)

# zad1(['exists', 'doesnt'])

def zad2():
    for root, files in os.walk('D:\Szkoła\Magisterka\Semestr1\WDJP\lab_10\data_for_lab_10'):
        for file in files:
            with open(os.path.join(root, file), 'r') as in_file:
                lines = [line.rstrip() for line in in_file]
            with open('plik.txt', 'a') as out_file:
                if os.path.getsize('D:\Szkoła\Magisterka\Semestr1\WDJP\lab_10\plik.csv') == 0:
                    out_file.writelines(line + '\n' for line in lines)
                else:
                    out_file.writelines(line + '\n' for line in lines[1::])

# zad2()

import time
from datetime import datetime
from zoneinfo import ZoneInfo
def zad3():
    data = input()
    ints = data.split(':')
    date = datetime(2023, 5, 11, int(ints[0]), int(ints[1]), int(ints[2]))
    print('Time in Tokyo: ' + date.astimezone(ZoneInfo('Asia/Tokyo')).strftime('%H:%M:%S'))
    print('Time in Sydney: ' + date.astimezone(ZoneInfo('Australia/Sydney')).strftime('%H:%M:%S'))
    print('Time in Waszyngton: ' + date.astimezone(ZoneInfo('America/New_York')).strftime('%H:%M:%S'))
    print('Time in London: ' + date.astimezone(ZoneInfo('Europe/London')).strftime('%H:%M:%S'))


# zad3()

# def zad4(birth):
#     delta = datetime.now() - birth
#     print(delta.days)
#     print(delta.)



def age(birth):
    today = datetime.now()
    years = today.year - birth.year
    months = 12 + today.month - birth.month
    days = today.day - birth.day
    print(today.year)
    print(today.month)
    print(today.day)
    # months = ((today.year - birth.year) * 12 + (today.month - birth.month))%12 - 1
    print(years)
    print(months)
    print(days)
    if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
        years -= 1



    return years, months, days

print(age(datetime(2000,1,1)))