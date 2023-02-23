intNumber1 = 6
floatNumber1 = 5.5

intNumber2 = int("10100", base=2)
floatNumber2 = 5.2

intNumber3 = 1
floatNumber3 = 0.5

intNumber4 = 0
floatNumber4 = 115.5


def exercise(int_number, float_number):
    print(int_number.bit_count())
    print(float_number.is_integer())


exercise(intNumber1, floatNumber1)
exercise(intNumber2, floatNumber2)
exercise(intNumber3, floatNumber3)
exercise(intNumber4, floatNumber4)
