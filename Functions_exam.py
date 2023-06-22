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
