# text = input()
# count = 0
# lst = []
# list_count = []
# letters_lower_eng = [chr(s).lower() for s in range(65, 91)]
# words_list = text.split()
# for word in words_list:
#     for s in word:
#         if s.isalpha():
#             count += 1
#     list_count.append({word: count})
#     count = 0
# for data in list_count:
#     for key, value in data.items():
#         key = key.lower()
#         for s in key:
#             for i, v in enumerate(letters_lower_eng):
#                 if s == v:
#                     i_shift = i + value
#                     if i_shift >= 26:
#                         i_shift -= 26
#                     s_shift = letters_lower_eng[i_shift]
#                     lst.append(s_shift)
# for i, v in enumerate(text):
#     if not v.isalpha():
#         lst.insert(i, v)
#     if v.isupper():
#         lst[i] = lst[i].upper()
# lst = ''.join(lst)
# print(lst)
text = input().lower().split()
str = []
letters_lower_eng = [chr(s).lower() for s in range(ord('a'), ord('z') + 1)]
for word in text:
    for letter in word:
        if letter in letters_lower_eng:
            str.append(''.join(letters_lower_eng).find(letter))
print(str)

print(0x1AF2)