# Zad 1
import string

original_list = [i for i in range(1, 11)]
new_list = original_list[5:]
original_list = original_list[:5]

# Zad 2
merged_list = original_list + new_list
merged_list.insert(0, 0)
print(sorted(merged_list, reverse=True))

# Zad 3
print("Podaj ciąg znaków:")
user_input = input()
unique_characters_lowercase = set(user_input.lower())
print(unique_characters_lowercase)

# Zad 4
months_pl = {
    1: 'Styczeń',
    2: 'Luty',
    3: 'Marzec',
    4: 'Kwiecień',
    5: 'Maj',
    6: 'Czerwiec',
    7: 'Lipiec',
    8: 'Sierpień',
    9: 'Wrzesień',
    10: 'Październik',
    11: 'Listopad',
    12: 'Grudzień'
}

# Zad 5
months = {
   'en': {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
    },
    'pl': {
    1: 'Styczeń',
    2: 'Luty',
    3: 'Marzec',
    4: 'Kwiecień',
    5: 'Maj',
    6: 'Czerwiec',
    7: 'Lipiec',
    8: 'Sierpień',
    9: 'Wrzesień',
    10: 'Październik',
    11: 'Listopad',
    12: 'Grudzień'
    }
}
print(months['pl'][4])
print(months['en'][4])

# Zad 6
name = 'Marianna'
name_unique_letters = sorted(set(name), key=name.index)
value = 1
dictionary = dict.fromkeys(name_unique_letters, value)
print(dictionary)

# Zad 7
print('Podaj ciąg znaków i/lub liczb: ')
user_input7 = input()
user_input7 = user_input7.lower()
digits = list(string.digits)
number_of_digits = len(digits)
ascii = list(string.ascii_lowercase)
number_of_ascii = len(ascii)

for x in user_input7:
    if x in digits:
        digits.remove(x)
    if x in ascii:
        ascii.remove(x)

print(f"Procent użytych cyfr {100 - len(digits)/number_of_digits*100}")
print(f"Procent użytych liter {100 - len(ascii)/number_of_ascii*100}")