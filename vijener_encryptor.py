#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан словарь русского алфавита.

alphabet_ru = {
    'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5,
    'ё': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11,
    'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17,
    'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23,
    'ч': 24, 'ш': 25, 'щ': 26, 'ь': 27, 'ъ': 28, 'э': 29,
    'ю': 30, 'я': 31,
}

ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Необходимо написать программу, шифрующее слово с помощью Шифра Виженера (https://is.gd/WEVeME) и
# (http://prntscr.com/nxuspd).

# Допускается:
#    - Использование цикла for и while;
#    - Использование условия if;
#    - Операции со словарем;
#    - Ввод только строчными буквами (НЕ использовать пробелы, прописные буквы);
#    - Слово должно состоять из букв русского алфавита.
#
# На выходе программа должна выдавать только результат.
#
# Алгоритм реализации:
# Пусть дано слово 'привет'.
# Пусть дан ключ 'скиллбокс'.
# Каждая буква в словаре букв алфавита является ключом к позиционном номеру этой буквы в алфавите.
# Суммируем позиции букв введенного слова и ключа по модулю N, где N - количество букв в алфавите:
# п + с = 16 + 18 = 34 mod 32 = 2 (буква 'п')
# р + к = 17 + 11 = 28 mod 32 = 28 (буква 'ъ')
# и т.д.

# -------------------------------------------------------------------------

# # MY DECISION AT THIS STAGE: Кодер шифра Виженера для русского алфавита

# message = input('Введите слово: ')
# key_message = input('Введите ключ: ')
# letter_ru = (list(alphabet_ru.keys()))

import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


class VijenerEnc:

    def __init__(self, user_word, key_word, alphabet):
        self.user_word = user_word
        self.key_word = key_word
        self.alphabet = alphabet
        self.index_word = []
        self.index_key = []

    def find_index(self, my_str, symbol):
        for i in symbol:
            start = my_str.find(i)
            yield start
            start += len(symbol)

    def get_key(self, value):
        for num in value:
            yield ru[num]

    def run(self):
        with Profiler() as p:
            total_index_1 = self.find_index(ru, self.user_word)
            total_index_2 = self.find_index(ru, self.key_word)
            a = [(i + j) % len(self.alphabet) for i, j in zip(total_index_1, total_index_2)]
            for i in self.get_key(a):
                print(i, end='')


if __name__ == "__main__":
    young_encryptor = VijenerEnc(user_word=input('Введите слово: '),
                                 key_word=input('Введите сдвиг: '),
                                 alphabet=ru)
    young_encryptor.run()

# ----------------------------------------------------------------------
# декодер шифра Виженера

#
# message = input('Введите слово: ')
# key_message = 'скиллбокс'
# letter_rus = (list(alphabet_ru.keys()))
#
#
# def get_key(alphabet_rus, value):
#     for key, number in alphabet_ru.items():
#         if number == value:
#             return key
#
#
# if len(message) > len(key_message):
#     index_key_message = 0
#     for char in range(len(message) - len(key_message)):
#         key_message += key_message[index_key_message]
#         index_key_message += 1
#
#
# new_letter = []
# new_key_letter = []
# for i2, key_letter in enumerate(key_message):
#     for char in letter_rus:
#         number_letter_key = char == key_letter
#         if number_letter_key:
#             new_key_letter.append(alphabet_ru.get(char))
#             break
#
# for i1, letter_message in enumerate(message):
#     for char in letter_rus:
#         number_letter = char == letter_message
#         if number_letter:
#             new_letter.append(alphabet_ru.get(char))
#             break
#
# initial_word = ''
# for index_initial_word, letter_initial_word in enumerate(new_letter):
#     initial_word_number = letter_initial_word + 32 - new_key_letter[index_initial_word]
#     if initial_word_number > 31:
#         initial_word += get_key(alphabet_ru, initial_word_number % 32)
#     else:
#         initial_word += get_key(alphabet_ru, initial_word_number)
#         continue
# print(initial_word)


# TODO дан словарь из английского алфавита. Попробовать кодер Виженера

# alphabet_eng = {
#     'a': 0,  'b': 1,  'c': 2,  'd': 3,  'e': 4,  'f': 5,
#     'g': 6,  'h': 7,  'i': 8,  'j': 9,  'k': 10, 'l': 11,
#     'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
#     's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
#     'y': 24, 'z': 25,
# }
