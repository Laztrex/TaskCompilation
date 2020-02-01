#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан словарь русского алфавита.

import alphabet_settings


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

class VijenerEnc:

    def __init__(self, user_word, key_word, mode='encode', alphabet='ru'):
        self.user_word = user_word
        self.key_word = key_word
        self.mode = mode
        self.alphabet = alphabet

    def _find_index(self, my_str, symbol, inverse=False):
        for i in symbol:
            start = my_str.find(i)
            if inverse:
                yield 0 - start
            else:
                yield start
            start += len(symbol)

    def run(self):
        if len(self.user_word) > len(self.key_word):
            self.key_word += self.key_word[:len(self.user_word) - len(self.key_word)]
        total_index_1 = self._find_index(self.alphabet, self.user_word)

        if self.mode == 'decode':
            total_index_2 = self._find_index(self.alphabet, self.key_word, inverse=True)
        else:
            total_index_2 = self._find_index(self.alphabet, self.key_word)

        for index_word, index_key in zip(total_index_1, total_index_2):
            print(self.alphabet[(index_word + index_key) % len(self.alphabet)], end='')


# permutation = [(index_word - index_key) % len(self.alphabet)
#               for index_word, index_key in zip(total_index_1, total_index_2)]


if __name__ == "__main__":
    young_encryptor = VijenerEnc(user_word=input('Введите слово: '),
                                 key_word=input('Введите сдвиг: '),
                                 mode='decode',
                                 alphabet=alphabet_settings.ru)
    young_encryptor.run()

# ----------------------------------------------------------------------

# TODO дан словарь из английского алфавита. Попробовать кодер Виженера

# alphabet_ru = {
#     'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5,
#     'ё': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11,
#     'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17,
#     'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23,
#     'ч': 24, 'ш': 25, 'щ': 26, 'ь': 27, 'ъ': 28, 'э': 29,
#     'ю': 30, 'я': 31,
# }


# alphabet_eng = {
#     'a': 0,  'b': 1,  'c': 2,  'd': 3,  'e': 4,  'f': 5,
#     'g': 6,  'h': 7,  'i': 8,  'j': 9,  'k': 10, 'l': 11,
#     'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
#     's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
#     'y': 24, 'z': 25,
# }
