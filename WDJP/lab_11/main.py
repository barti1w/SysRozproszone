import re

def zad1():
    digits = re.compile('[0-9]')
    threeDigits = re.compile('[0-9]{3}')
    ipvFour = re.compile('[01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]')
    bigFirstLetter = re.compile('[A-Z][a-z]*')
    fourWords = re.compile("[A-z0-9]*[ ][A-z0-9]*[ ][A-z0-9]*[ ][A-z0-9]*")
    url = re.compile("^https://")

    with open("strings.txt", 'r') as file:
        for line in file:

            print('Line:', line)

            if re.findall(digits, line):
                print('Digit:', re.findall(digits, line))

            if re.findall(threeDigits, line):
                print('ThreeDigits:', re.findall(threeDigits, line))

            if re.match(ipvFour, line):
                print('IPv4:', re.match(ipvFour, line).string)

            if re.findall(bigFirstLetter, line):
                print('BigFirstLetter:', re.findall(bigFirstLetter, line))

            if re.match(fourWords, line):
                print('fourWords:', re.match(fourWords, line).string)

            if re.match(url, line):
                print('url:', re.match(url, line).string)


def zad2():

    date = re.compile('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[ ][0-3][0-9]')
    ip = re.compile('ip-[0-9]{3}[-][0-9]{3}[-][0-9]{3}')

    with open("auth.log", 'r') as file:
        for line in file:

            # if re.match(date, line):
            #     print(re.match(date, line).group())

            if re.findall(ip, line):
                print(re.findall(ip, line))

zad2()