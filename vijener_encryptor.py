#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан словарь русского алфавита.
import re

import alphabet_settings
from string import punctuation

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
# п + с = 16 + 18 = 34 mod 32 = 2 (буква 'б')
# р + к = 17 + 11 = 28 mod 32 = 28 (буква 'ъ')
# и т.д.

# -------------------------------------------------------------------------


class VijenerEnc:

    def __init__(self, word, key, mode='encode', alphabet='ru', sign=None):
        word = word.replace(' ', '')
        self.key_word = key
        self.mode = mode
        self.alphabet = alphabet
        self.alphabet_dict = {}
        self.dict_punc = {b.group(): b.span()[0] for b in re.finditer(f'[{punctuation}]', word) if b.group()
                          in punctuation} if sign else None
        tt = str.maketrans(dict.fromkeys(punctuation))
        self.word_list = word.translate(tt)
        self.key_list = list(key)
        self.a = []

    def _find_index(self, my_str, symbol, inverse=False):
        restart = 0
        while True:
            for i, letter in enumerate(symbol[restart:]):
                start = my_str.find(letter.lower())
                if start == -1:
                    self._check_alphabet(letter)
                    my_str = self.alphabet
                    restart += i
                    break
                elif inverse:
                    yield 0 - start
                else:
                    yield start
            else:
                break

    def run(self):
        self._check_alphabet()
        if len(self.word_list) > len(self.key_word):
            self.key_word += self.key_word * (len(self.word_list) // len(self.key_word))
        total_index_1 = self._find_index(self.alphabet, self.word_list)

        if self.mode == 'decode':
            total_index_2 = self._find_index(self.alphabet, self.key_word, inverse=True)
        else:
            total_index_2 = self._find_index(self.alphabet, self.key_word)

        secret_word = ''
        for index_word, index_key in zip(total_index_1, total_index_2):
            secret_word += self.alphabet[(index_word + index_key) % len(self.alphabet)]
            # print(secret_word, end='')
        if not self.dict_punc:
            return secret_word
        return "".join(secret_word[:idx] + sign + secret_word[idx:] for sign, idx in self.dict_punc.items())

    def _set_alphabet(self):
        if self.alphabet == 'ru':
            self.alphabet = alphabet_settings.ru
        else:
            self.alphabet = alphabet_settings.eng

    def _check_alphabet(self, check_letter=None):
        if check_letter:
            if check_letter.isalpha():
                if check_letter.lower() not in self.alphabet:
                    self.alphabet = alphabet_settings.ru if check_letter.lower() in alphabet_settings.ru \
                        else alphabet_settings.eng
                    return self.alphabet
            else:
                return False

        if self.alphabet == 'ru':
            self.alphabet = alphabet_settings.ru
        else:
            self.alphabet = alphabet_settings.eng


if __name__ == '__main__':
    analyze = VijenerEnc(word='скилл- бокс', key='привет', sign=True)
    print(analyze.run())
# permutation = [(index_word - index_key) % len(self.alphabet)
#               for index_word, index_key in zip(total_index_1, total_index_2)]
