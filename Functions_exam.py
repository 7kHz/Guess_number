# def draw_triangle(n):
#     for i in range(n):
#         print(' ' * (n - 1 - i) + '*' * (i * 2 + 1))
#
#
# draw_triangle(8)

# def get_shipping_cost(quantity):
#     result = 1000 + 120 * (quantity - 1)
#     return result
#
#
# print(get_shipping_cost(41))

# from math import factorial
#
#
# def compute_binom(n, k):
#     result = int(factorial(n) / (factorial(k) * factorial(n - k)))
#     return result
#
#
# print(compute_binom(100, 3))


# def number_to_words(num):
#     tens = {10: 'десять',
#             20: 'двадцать',
#             30: 'тридцать',
#             40: 'сорок',
#             50: 'пятьдесят',
#             60: 'шестьдесят',
#             70: 'семьдесят',
#             80: 'восемьдесят',
#             90: 'девяносто'}
#     ones = {1: 'один',
#             2: 'два',
#             3: 'три',
#             4: 'четыре',
#             5: 'пять',
#             6: 'шесть',
#             7: 'семь',
#             8: 'восемь',
#             9: 'девять'}
#     teens = {11: 'одиннадцать',
#              12: 'двенадцать',
#              13: 'тринадцать',
#              14: 'четырнадцать',
#              15: 'пятнадцать',
#              16: 'шестнадцать',
#              17: 'семнадцать',
#              18: 'восемнадцать',
#              19: 'девятнадцать'}
#     if num % 10 == 0:
#         return tens[num]
#     if num % 10 != 0 and 10 < num < 20:
#         return teens[num]
#     if num <= 9:
#         return ones[num]
#     else:
#         tens_count = num // 10 * 10
#         ones_count = num % 10
#         return f'{tens[tens_count]} {ones[ones_count]}'
#
#
# print(number_to_words(12))


# def get_month(language, number):
#     d = {'ru': {1: 'январь',
#                 2: 'февраль',
#                 3: 'март', 4: 'апрель',
#                 5: 'май', 6: 'июнь',
#                 7: 'июль', 8: 'август',
#                 9: 'сентябрь',
#                 10:'октябрь',
#                 11: 'ноябрь',
#                 12: 'декабрь'},
#
#          'en': {1: 'january',
#                 2: 'february',
#                 3: 'march',
#                 4: 'april',
#                 5: 'may',
#                 6: 'june',
#                 7: 'july',
#                 8: 'august',
#                 9: 'september',
#                 10: 'october',
#                 11: 'november',
#                 12: 'december'}}
#
#     return d[language][number]
#
#
# print(get_month('en', 5))

# def is_magic(date: str) -> [int]:
#     date = date.split('.')
#     date_int = [int(d) for d in date]
#     if date_int[0] * date_int[1] == date_int[2] % 100:
#         return True
#     return False
#
#
# print(is_magic('11.06.1960'))

#
# def is_pangram(text: str):
#     letters_example = [chr(i) for i in range(97, 123)]
#     letters = [i.lower() for i in text if i.isalpha()]
#     for i, v in enumerate(letters):
#         if v in letters_example:
#             letters_example.remove(v)
#     if letters_example:
#         return False
#     return True
#
#
# print(is_pangram('Crazy Fredrick bought many very exquisite opal jewels'))


# from math import log2, ceil
#
# n = int(input())
# result = ceil(log2(n))
# print(result)
import random

print('Добро пожаловать в числовую угадайку\nВведите число от 1 до 10:')
rand_num = random.randrange(1, 11)


def is_valid(num):
    if 1 <= num <= 10:
        return True
    return False


def input_num(num):
    while True:
        if is_valid(num):
            break
        else:
            print('А может быть все-таки введем целое число от 1 до 10?')
            num = int(input())
    return num


def guess_num(num):
    count = 0
    while True:
        if num < rand_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            num = int(input())
            count += 1
        if num > rand_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            num = int(input())
            count += 1
        if num == rand_num:
            print(f'Вы угадали число за {count + 1} попыток, поздравляем!')
            return True


while True:
    try:
        n = int(input())
        if guess_num(input_num(n)):
            break
    except ValueError:
        print('Введите число:')
