#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import shuffle, seed

import alphabet_settings


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

# --------------------------------------------------------------------------------


class CaesarEncrypt:

    def __init__(self, word, key, mode, alphabet='ru', jeff=None):
        self.state = mode
        self.mode_alpha = alphabet
        self.alphabet = {}
        self.user_word = word.replace(' ', '')
        self.shift = int(key)
        self.jeff_mode_n = jeff
        self.discs = None

    def run(self):
        if self.jeff_mode_n:
            self.discs = [
                self.set_alphabet(user_alphabet=self.disc_generator(
                    alphabet_settings.ru if self.mode_alpha == 'ru' else alphabet_settings.eng))
                for _ in range(self.jeff_mode_n)
            ]
        self.set_alphabet()
        if self.state == 'dec':
            self.shift = 0 - self.shift
        return self.encoder() if not self.jeff_mode_n else self.jefferson_encryption()

    def encoder(self):
        secret_word = ''

        for letter in self.user_word.lower():
            # if letter.isalpha():
            secret_word += self._secret_permutation(letter)

        return secret_word

    def set_alphabet(self, user_alphabet=None):
        if user_alphabet:
            return {i: char for i, char in
                    enumerate(user_alphabet)}
        if self.mode_alpha == 'ru':
            self.alphabet = {i: char for i, char in
                             enumerate(alphabet_settings.ru)}
        else:
            self.alphabet = {i: char for i, char in
                             enumerate(alphabet_settings.eng)}

    def _check_alphabet(self, check_letter=None):
        if check_letter:
            if check_letter.isalpha() and check_letter not in self.alphabet:
                self.mode_alpha = 'ru' if check_letter in alphabet_settings.ru \
                    else 'eng'
                self.set_alphabet()
                return False
            else:
                return True

    def _secret_permutation(self, letter):
        for num, char in self.alphabet.items():
            if char == letter:
                return self.alphabet[(num + self.shift) % len(self.alphabet)]
            # return ''
        else:
            if letter.isnumeric():
                return letter
            elif not self._check_alphabet(letter):
                return self._secret_permutation(letter=letter)
            else:
                return ''

    def disc_generator(self, clear_alphabet):
        seed(42)
        list_str = list(clear_alphabet)
        shuffle(list_str)
        return ''.join(list_str)

    def jefferson_encryption(self):
        secret_word = ''
        text = self.user_word
        for i in range(len(text)):
            self.user_word, self.alphabet = text[i], self.discs[i % self.jeff_mode_n]
            secret_word += self.encoder()
        return secret_word

# """
#  Пример:
# # message_encrypt = 'фхнжйч'
# # shift_encrypt = 5
# # Вывод: Зашифрованным словом было - привет
# """
