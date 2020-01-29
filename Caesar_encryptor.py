#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан русский алфавит.

alphabet = [
    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
]

# Необходимо написать программу, шифрующее слово с помощью Шифра Цезаря(https://is.gd/rcGAsp).
# Программа должна принимать на вход от пользователя слово и число сдвигов.
#
# Допускается:
#    - Использование цикла for;
#    - Операции со списками;
#    - Ввод только строчными буквами (НЕ использовать пробелы, прописные буквы);
#    - Слово должно состоять из букв русского алфавита.
#
# На выходе программа должна выдавать только результат.
#
# Для примера:
# [
# абвгдеёжзийклмнопрстуфхцчшщъыьэюя,
# бвгдеёжзийклмнопрстуфхцчшщъыьэюяа,
# вгдеёжзийклмнопрстуфхцчшщъыьэюяаб,
# вгдеёжзийклмнопрстуфхцчшщъыьэюяаб,
# ]
#
# Слово:          скиллбокс
# Число сдвигов:  3
# Вывод:          фнлоодснф

message = input('Введите слово: ')
shift = int(input('Введите сдвиг: '))

# --------------------------------------------------------------------------------
# MY DECISION AT THIS STAGE:

# CODER

for element in range(shift):
    shift_alphabet = alphabet[0][element + 1:] + alphabet[0][:element + 1]
    if element > 31:
        if element == 32:   # Не нравится мне этот метод решения проблемы shift > числа элементов списка :(
            alphabet.append(shift_alphabet) # ух как не нравится!
        else:
            shift_alphabet = alphabet[0][(element % 32):] + alphabet[0][:(element % 32)] #фууу
            alphabet.append(shift_alphabet)
            continue
    alphabet.append(shift_alphabet)

index = 0
secret_word = ''
for letter in message:
    for char in alphabet[0]:
        index += 1
        new_letter = char == letter
        if new_letter:
            new_message = alphabet[shift][index - 1]
            secret_word += new_message
            index = 0
            break
        else:
            continue

print(secret_word)

# ------------------------------------------------
# DECODER.
#
# Необходимо написать программу, которая расшифровывает заданное зашифрованное слово силами Шифра Цезаря
# Подробнее о шифре Цезаря - (https://is.gd/rcGAsp).
# Дано зашифрованное сообщение, число сдвигов и русский алфавит
#
# Пример:
# message_encrypt = 'фхнжйч'
# shift_encrypt = 5
# Вывод: Зашифрованным словом было - привет

# -----------------------------------------------

# КОД программы

# message_encrypt = 'фнлоодснф'
# shift_encrypt = 3
#
# for element in range(shift):
#     shift_alphabet = alphabet[0][element + 1:] + alphabet[0][:element + 1]
#     alphabet.append(shift_alphabet)
#
#
# index = 0
# secret_word = ''
# for letter in message_encrypt:
#     for char in alphabet[shift_encrypt]:
#         index += 1
#         new_letter = char == letter
#         if new_letter:
#             new_message = alphabet[0][index - 1]
#             secret_word += new_message
#             index = 0
#             break
#         else:
#             continue
#
# print('Зашифрованным словом было -', secret_word)

# TODO ввести проверку принадлежности символа алфавиту
# TODO включить возможность ввода целого предложения с пробелами и знаками препинания (которые тоже будут шифроваться)
# TODO добавить английский алфавит
