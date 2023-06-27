# import random
#
# answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
#            "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
#            "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
#            "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
#
#
# def hello():
#     print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
#     user_name = input('Введите свое имя: ')
#     print(f'Hello {user_name}\n')
#     print('Для выхода нажмите "q"')
#
#
# def magic_ball():
#     while True:
#         question = input('Задайте свой вопрос: ')
#         answer = random.choice(answers)
#         if question == 'q':
#             print('До новых встреч!')
#             break
#         print(answer)
#
# hello()
# magic_ball()

# from random import randint
#
# print("".join([chr(randint(1, 127)) for i in range(int(input("Enter length of pass: ")))]))

# const_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# const_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
# eng_chars = 'abcdefghijklmnopqrstuvwxyz'
# chars = '.!, '
#
# text = "Hawnj pk swhg xabkna ukq nqj."
#
# const_lower_list = [s for s in eng_chars]
# letters_list = [s.lower() for s in text]
# n = 0
# while n < 26:
#     lst = []
#     for i, v in enumerate(text):
#         if v in eng_chars:
#             index = const_lower_list.index(v) - n
#             if index < 0:
#                 index = index + 26
#             lst.append(const_lower_list[index])
#     str_ = ''.join(lst)
#     print(str_)
#     n += 1


text = input()
words_dict = {}
count = 0
lst = []
letters_upper_eng = [chr(s) for s in range(65, 91)]
letters_lower_eng = [chr(s).lower() for s in range(65, 91)]
words_list = text.split()
for word in words_list:
    for s in word:
        if s.isalpha():
            count += 1
        words_dict[word] = count
    count = 0
for key, value in words_dict.items():
    key = key.lower()
    for s in key:
        for i, v in enumerate(letters_lower_eng):
            if s == v:
                i_shift = i + value
                if i_shift >= 26:
                    i_shift -= 26
                result = letters_lower_eng[i_shift]
                lst.append(result)
print(words_list)
